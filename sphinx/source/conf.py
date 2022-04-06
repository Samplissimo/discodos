# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Recommonmark extension imports
#import recommonmark
#from recommonmark.transform import AutoStructify

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'DiscoDOS - the geekiest DJ tool on the planet'
copyright = '2018-2021, J0J0 Todos'
author = 'J0J0 Todos'

# The short X.Y version
version = '1.0'

# The full version, including alpha/beta/rc tags
release = '1.1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    #'sphinxarg.ext',
    'sphinxcontrib.autoprogram',
    #'recommonmark'
    'myst_parser'
]

#source_suffix = {
#    '.rst': 'restructuredtext',
#    '.md': 'markdown',
#}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Extension configuration -------------------------------------------------

# Recommonmark configuration
#github_doc_root = 'https://github.com/joj0/discodos/tree/master/sphinx/source'
#def setup(app):
#    app.add_config_value('recommonmark_config', {
#            #'url_resolver': lambda url: github_doc_root + url,
#            'auto_toc_tree_section': 'Contents',
#            'enable_math': False,
#            'enable_inline_math': False,
#            'enable_eval_rst': True,
#            'enable_auto_doc_ref': True,  # deprecated
#    }, True)
#    app.add_transform(AutoStructify)

# MyST configuration
myst_heading_anchors = 7
myst_enable_extensions = [
    "strikethrough",
]
