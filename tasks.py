"""invoke tasks for the Pelican site.

These mirror the Makefile targets and are useful when you prefer
running Python over ``make``. Install with ``pip install invoke`` and
run ``invoke -l`` to list the available tasks.
"""
from __future__ import annotations

import os
from pathlib import Path

from invoke import task

BASE_PATH = Path(__file__).resolve().parent
PELICAN = "pelican"
PELICANOPTS = ""

INPUTDIR = str(BASE_PATH / "content")
OUTPUTDIR = str(BASE_PATH / "output")
CONFFILE = str(BASE_PATH / "pelicanconf.py")
PUBLISHCONF = str(BASE_PATH / "publishconf.py")


@task
def html(c):
    """Build the site with the development config."""
    c.run(f"{PELICAN} {INPUTDIR} -o {OUTPUTDIR} -s {CONFFILE} {PELICANOPTS}")


@task
def clean(c):
    """Remove the generated output directory."""
    if os.path.isdir(OUTPUTDIR):
        c.run(f"rm -rf {OUTPUTDIR}")


@task
def regenerate(c):
    """Regenerate the site on every content change (no live server)."""
    c.run(f"{PELICAN} -r {INPUTDIR} -o {OUTPUTDIR} -s {CONFFILE} {PELICANOPTS}")


@task
def serve(c):
    """Serve the site at http://localhost:8000 (rebuild manually)."""
    c.run(f"{PELICAN} -l {INPUTDIR} -o {OUTPUTDIR} -s {CONFFILE} {PELICANOPTS}")


@task
def serve_global(c, server="0.0.0.0"):
    """Serve the site on the given bind address (default 0.0.0.0)."""
    c.run(f"{PELICAN} -l {INPUTDIR} -o {OUTPUTDIR} -s {CONFFILE} {PELICANOPTS} -b {server}")


@task
def devserver(c):
    """Auto-regenerate + serve at http://localhost:8000."""
    c.run(f"{PELICAN} -lr {INPUTDIR} -o {OUTPUTDIR} -s {CONFFILE} {PELICANOPTS}")


@task
def publish(c):
    """Build the site with the production config."""
    c.run(f"{PELICAN} {INPUTDIR} -o {OUTPUTDIR} -s {PUBLISHCONF} {PELICANOPTS}")
