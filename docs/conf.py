# Configuration file for the Sphinx documentation builder.
# http://www.sphinx-doc.org/en/master/config

# -- Path setup

import os
import sys

sys.path.insert(0, os.path.abspath("../backend"))


# -- Project information

project = "repertoire"
copyright = "2021, blissful"
author = "blissful"
release = "0.2.0"

# -- General configuration

extensions = [
    # "sphinx_js",  # Broken atm, doesn't work with React
    "sphinx.ext.autodoc",
    "sphinxcontrib.autohttp.flask",
    "sphinx_rtd_theme",
    "sphinx_autodoc_typehints",
    "autodocsumm",
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
source_suffix = ".rst"
master_doc = "index"

# -- Configure sphinx_js

js_language = "typescript"
js_source_path = "../frontend/src"

# -- Configure autodoc

autodoc_default_options = {
    "autosummary-no-nesting": True,
}
typehints_fully_qualified = True

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
