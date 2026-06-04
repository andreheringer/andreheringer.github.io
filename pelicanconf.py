"""Pelican configuration for the Andre Heringer blog.

Settings are written so the same file can be used for local development
(``make html`` / ``make serve``) and for production (``make publish``,
which loads ``publishconf.py`` on top of this).
"""
from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path

# --- Paths --------------------------------------------------------------
BASE_PATH = Path(__file__).resolve().parent
CONTENT_PATH = BASE_PATH / "content"
OUTPUT_PATH = BASE_PATH / "output"

PATH = str(CONTENT_PATH)
OUTPUT_PATH = str(OUTPUT_PATH)

# --- Site metadata ------------------------------------------------------
AUTHOR = "Andre Heringer"
SITENAME = "Andre Heringer"
SITESUBTITLE = "Paper scrap pile of ideas from my head"
SITEURL = ""

TIMEZONE = "America/Sao_Paulo"
DEFAULT_LANG = "en"
LOCALE = ("en_US.UTF-8", "C.UTF-8", "C")

# Default publication date used when a post omits ``Date``.
DEFAULT_DATE_FORMAT = "%B %-d, %Y"

# --- Theme --------------------------------------------------------------
# The custom ``ps-minimal`` theme lives at ``themes/ps-minimal``. It is
# inspired by the PlanetScale blog (light, Inter + Cascadia Code, single
# orange accent).
THEME = "themes/ps-minimal"

# --- Plugins ------------------------------------------------------------
# Plugins live under ``plugins/`` and are activated here. The
# ``relative_url`` plugin below adds a Jinja filter that resolves
# site-relative URLs (e.g. ``/about/``) into paths relative to the
# currently-rendered page.
PLUGIN_PATHS = [str(BASE_PATH / "plugins")]
PLUGINS = ["relative_url"]
PLUGINS_CACHE_PATH = str(BASE_PATH / ".cache")

# --- Content behaviour --------------------------------------------------
DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 50

# Templates Pelican should generate in addition to article and page outputs.
DIRECT_TEMPLATES = ("index", "categories", "tags", "authors", "archives")

# Paginated article listings (each gets its own page1, page2, …).
PAGINATED_TEMPLATES = {
    "index": None,
    "tag": None,
    "category": None,
    "author": None,
}

# A post is considered a draft unless ``Status: published`` is set.
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = "Misc"

# Display *pages* (not just articles) in the navigation menu. The nav
# is driven entirely by ``MENUITEMS`` below, so we don't auto-list pages.
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Save pages at the root using pretty URLs: ``content/pages/about.md``
# becomes ``output/about/index.html`` rather than the default
# ``output/pages/about.html``.
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# Navigation: order is preserved by the template.
MENUITEMS = (
    ("About", "/about/"),
    ("GitHub", "https://github.com/andreheringer"),
    ("YouTube", "https://www.youtube.com/@aagheringer"),
)

# --- Feeds --------------------------------------------------------------
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ATOM = "feeds/atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# --- Social links shown in the sidebar ---------------------------------
SOCIAL = (
    ("GitHub", "https://github.com/andreheringer"),
)

# --- Markdown extensions ------------------------------------------------
# Pelican 4.9+ uses a structured MARKDOWN dict rather than the legacy
# ``MD_EXTENSIONS`` list. See the Pelican docs for the full schema.
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.toc": {"permalink": True, "toc_depth": "2-3"},
    },
    "extensions": [
        "markdown.extensions.fenced_code",
        "markdown.extensions.codehilite",
        "markdown.extensions.tables",
        "markdown.extensions.toc",
        "markdown.extensions.extra",
        "markdown.extensions.smarty",
        "markdown.extensions.sane_lists",
    ],
}

# --- Jinja globals ------------------------------------------------------
# Expose ``now()`` so the footer can render the current year without
# needing a static value.
JINJA_GLOBALS = {
    "now": lambda: __import__("datetime").datetime.now(),
}

# --- Typographic niceties ----------------------------------------------
TYPOGRIFY = True

# --- Static / extras ----------------------------------------------------
# Files placed under ``content/extra/`` are copied verbatim to the
# output root. Useful for a ``robots.txt`` or ``CNAME``.
STATIC_PATHS = ["extra"]
EXTRA_PATH_METADATA: dict[str, dict[str, str]] = {}

# Delete the output directory before each fresh build when running
# ``make html``.
DELETE_OUTPUT_DIRECTORY = False

# Tell Pelican about our build year so templates can use ``{{ now() }}``.
YEAR = datetime.now().year

# --- Slim reStructuredText options --------------------------------------
DOCUTILS_SETTINGS: dict[str, object] = {}
