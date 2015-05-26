=============================
Django Sponsors
=============================

.. image:: https://badge.fury.io/py/django-sponsors.png
    :target: https://badge.fury.io/py/django-sponsors

.. image:: https://travis-ci.org/miguelfg/django-sponsors.png?branch=master
    :target: https://travis-ci.org/miguelfg/django-sponsors

.. image:: https://coveralls.io/repos/miguelfg/django-sponsors/badge.png?branch=master
    :target: https://coveralls.io/r/miguelfg/django-sponsors?branch=master

Django App to manage project sponsors

Documentation
-------------

The full documentation is at https://django-sponsors.readthedocs.org.

Quickstart
----------

Install Django Sponsors::

    pip install django-sponsors

Then use it in a project:

To show all sponsors in uncategorized way::

    {% show_sponsors %}

To show only platinum sponsors with its default platinum styles (see sponsors.css)::

    {% show_sponsors 'platinum' %}

To show gold and silver sponsors with their default gold and silver styles (see sponsors.css)::

    {% show_sponsors 'gold,silver' %}


Features
--------
* Template Tags
* Models


TODOs
-----
* Use thumbnails?
* More testing
* More documentation
* Sponsor Join Form
* Sponsor Join View
