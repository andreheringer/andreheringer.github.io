"""Production overrides loaded on top of ``pelicanconf.py`` via
``pelican content -s publishconf.py``.

The key change is enabling relative URLs (so the generated site works
no matter what subpath GitHub Pages serves it from) and pinning the
canonical ``SITEURL``.
"""
from __future__ import annotations

import sys
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
sys.path.append(str(BASE_PATH))

from pelicanconf import *  # noqa: F401,F403

SITEURL = "https://andreheringer.github.io"
RELATIVE_URLS = True

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ATOM = "feeds/atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# When using a custom domain, drop a ``CNAME`` file under
# ``content/extra/`` and Pelican will copy it as-is.
DISQUS_SITENAME = None
GOOGLE_ANALYTICS = None

# Ensure feeds are generated with absolute URLs even when RELATIVE_URLS
# is on (Pelican handles this through FEED_DOMAIN above).
