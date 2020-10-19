# Configuration file for the Sphinx documentation builder.
# http://www.sphinx-doc.org/en/master/config

# -- Path setup

import os
import sys

sys.path.insert(0, os.path.abspath("../"))


# -- Project information

project = "repertoire"
copyright = "2020, azuline"
author = "azuline"
release = "0.2.0"

# -- General configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_rtd_theme",
    "sphinx_autodoc_typehints",
    "sphinx_automodapi.automodapi",
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
source_suffix = ".rst"
master_doc = "index"

# -- Configure sphinx_autodoc_typehints

typehints_fully_qualified = True


# Monkey patch sphinx_automodapi
# https://github.com/astropy/sphinx-automodapi/issues/119


def patch_automodapi(app):
    """Monkey-patch the automodapi extension to exclude imported members"""
    from sphinx_automodapi import automodsumm
    from sphinx_automodapi.utils import find_mod_objs

    automodsumm.find_mod_objs = lambda *args: find_mod_objs(args[0], onlylocals=True)


def setup(app):
    app.connect("builder-inited", patch_automodapi)


# -- Options for HTML output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
