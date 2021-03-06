import doctest
from datetime import datetime

import serde_ext


# Project configuration
project = 'Serde-Ext'
copyright = '%d, %s' % (datetime.now().year, serde_ext.__author__)
author = serde_ext.__author__
version = serde_ext.__version__
release = serde_ext.__version__

# General configuration
default_role = 'obj'
doctest_default_flags = (
    doctest.DONT_ACCEPT_TRUE_FOR_1
    | doctest.ELLIPSIS
    | doctest.NORMALIZE_WHITESPACE
)
doctest_global_setup = 'from serde-ext import *'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'serde': ('https://ross.macarthur.io/project/serde/', None)
}
master_doc = 'index'
autodoc_member_order = 'bysource'
napoleon_include_init_with_doc = True

# HTML configuration
html_theme = 'alabaster'
html_theme_options = {
    'fixed_sidebar': True,
    'logo_name': True,
    'github_user': 'rossmacarthur',
    'github_repo': 'serde-ext',
    'page_width': '1000px',
    'sidebar_width': '200px'
}
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html'
    ]
}
html_static_path = ['static']
