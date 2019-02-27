Serde-Ext
=========

.. image:: https://img.shields.io/pypi/v/serde-ext.svg?style=flat-square&colorB=4c1
    :target: https://pypi.org/project/serde-ext/
    :alt: PyPI Version

.. image:: https://img.shields.io/badge/docs-passing-brightgreen.svg?style=flat-square
    :target: https://ross.macarthur.io/project/serde-ext/
    :alt: Documentation Status

.. image:: https://img.shields.io/travis/rossmacarthur/serde-ext/master.svg?style=flat-square
    :target: https://travis-ci.org/rossmacarthur/serde-ext
    :alt: Build Status

.. image:: https://img.shields.io/codecov/c/github/rossmacarthur/serde-ext.svg?style=flat-square
    :target: https://codecov.io/gh/rossmacarthur/serde-ext
    :alt: Code Coverage

Extended classes and functions for use with Serde_.

Getting started
---------------

Install this package as a Serde_ feature

::

    pip install serde[ext]


The additional fields and validators provided will be re-exported

.. code:: python

    from serde import Model, fields

    class Person(Model):
        name = fields.Str()
        email = fields.Email()
        website = fields.Optional(fields.Url)


View the latest usage and API documentation
`here <https://ross.macarthur.io/project/serde-ext/api.html>`_.

License
-------

This project is licensed under the MIT License.

.. _Serde: https://github.com/rossmacarthur/serde
