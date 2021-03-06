"""
Setup file for Serde-Ext.
"""

import io
import os
import re

from setuptools import find_packages, setup


def get_metadata():
    """
    Return metadata for Serde-Ext.
    """
    here = os.path.abspath(os.path.dirname(__file__))
    init_path = os.path.join(here, 'src', 'serde_ext', '__init__.py')
    readme_path = os.path.join(here, 'README.rst')

    with io.open(init_path, encoding='utf-8') as f:
        about_text = f.read()

    metadata = {
        key: re.search(r'__' + key + r'__ = ["\'](.*?)["\']', about_text).group(1)
        for key in ('title', 'version', 'url', 'author', 'author_email', 'license', 'description')
    }
    metadata['name'] = metadata.pop('title')

    with io.open(readme_path, encoding='utf-8') as f:
        metadata['long_description'] = f.read()

    return metadata


metadata = get_metadata()

# Primary requirements
install_requires = [
    'serde >=0.4.0',
    'validators >=0.12.0, <0.13.0'
]

# Development requirements
lint_requires = [
    'flake8 >=3.7.0',
    'flake8-docstrings',
    'flake8-isort',
    'flake8-quotes',
    'pep8-naming'
]
test_requires = [
    'mock',
    'pytest >=3.6.0',
    'pytest-cov >= 2.6.1',
    'pytest-doctest-import'
]

setup(
    # Options
    install_requires=install_requires,
    extras_require={
        'dev.lint': lint_requires,
        'dev.test': test_requires
    },
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    packages=find_packages('src'),
    package_dir={'': 'src'},

    # Metadata
    download_url='{url}/archive/{version}.tar.gz'.format(**metadata),
    project_urls={
        'Documentation': 'https://ross.macarthur.io/project/serde-ext/',
        'Issue Tracker': '{url}/issues'.format(**metadata)
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords='serde serialization deserialization validation schema json',
    **metadata
)
