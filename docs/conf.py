# -*- coding: utf-8 -*-
#
# Screenflow documentation build configuration file, created by
# sphinx-quickstart on Thu Mar  9 15:20:09 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
from os.path import join, abspath

sys.path.insert(0, join(abspath('.'), 'screenflow'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
]

source_suffix = '.rst'
master_doc = 'index'
project = u'Screenflow'
copyright = u'2017, Félix Voituret'
author = u'Félix Voituret'
version = u'1.0'
release = u'1.0.0'
language = None
exclude_patterns = ['_build']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'default'
htmlhelp_basename = 'Screenflo documentation'

latex_documents = [
    (master_doc, 'Screenflow.tex', u'Screenflow Documentation',
     u'Félix Voituret', 'manual'),
]


man_pages = [
    (master_doc, 'screenflow', u'Screenflow Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'Screenflow', u'Screenflow Documentation',
     author, 'Screenflow', 'One line description of project.',
     'Miscellaneous'),
]