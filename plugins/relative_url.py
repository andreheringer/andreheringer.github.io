"""relative_url plugin for Pelican.

Adds a ``relative_url`` Jinja filter that resolves a site-relative URL
(``/about/``, ``/feeds/atom.xml``) into a path relative to the current
page being rendered. Pelican's own ``SITEURL`` is page-relative when
``RELATIVE_URLS`` is True, but the filter still works in dev mode
(absolute ``SITEURL``) by recomputing the path from the page URL.
"""
from __future__ import annotations

import posixpath
from typing import Any

from jinja2 import pass_context
from pelican import signals


@pass_context
def _relative_url(context: dict, target: Any) -> str:
    if not target:
        return ""
    target = str(target)

    if target.startswith("./") or target.startswith("../"):
        return target

    # Normalise to a site-relative form. Pelican's ``page.url`` returns
    # the URL without a leading slash (e.g. ``about/``); raw strings
    # may already start with ``/``.
    if not target.startswith("/"):
        target = "/" + target

    # ``posixpath`` treats a leading ``/`` as the filesystem root and
    # then computes ``..`` chains when mixed with a non-root start path.
    # Strip the leading slash so the computation stays in a relative
    # namespace.
    site_path = target.lstrip("/")

    current = context.get("output_file")
    if not current:
        for key in ("article", "page"):
            obj = context.get(key)
            if obj is not None and getattr(obj, "save_as", None):
                current = obj.save_as
                break

    if not current:
        return target

    current_dir = posixpath.dirname(current) or "."

    # The site root: ``/`` (or no path) — compute the relative path from
    # ``current_dir`` to ``.`` (the site root).
    if not site_path or site_path == ".":
        return posixpath.relpath(".", current_dir)

    rel = posixpath.relpath(site_path, current_dir)
    return rel if rel != "." else "."


def _register(pelican_obj):
    pelican_obj.env.filters["relative_url"] = _relative_url


def register() -> None:
    signals.generator_init.connect(_register)
