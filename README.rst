=============================
Django Sponsors
=============================

.. image:: https://badge.fury.io/py/django-sponsors.png
    :target: https://badge.fury.io/py/django-sponsors

.. image:: https://travis-ci.org/miguelfg/django-sponsors.png?branch=master
    :target: https://travis-ci.org/miguelfg/django-sponsors

.. image:: https://coveralls.io/repos/miguelfg/django-sponsors/badge.png?branch=master
    :target: https://coveralls.io/r/miguelfg/django-sponsors?branch=master

Django App to easily manage Django projects sponsors

Documentation
-------------

The full documentation is at https://django-sponsors.readthedocs.org.

Quickstart
----------

Install Django Sponsors:

1. Using pip::

    pip install django-sponsors

2. Add the ``sponsors`` application to ``INSTALLED_APPS`` in your settings file::

    INSTALLED_APPS = (
        ...
        'sponsors',
        ...
    )
3. Sync database::

    ``$ ./manage.py syncdb``  or
    ``$ ./manage.py migrate``

**Important:** South 1.0 or greater is required to run migrations.

4. Run the collectstatic management command::

    ``$ /manage.py collectstatic``

This will copy static sponsors.css into the directory given by the STATIC_ROOT setting.

5. Load in your template the sponsors.css file like this::

    <link rel="stylesheet" href="{% static "sponsors/css/sponors.css" %}">

This will copy static sponsors.css into the directory given by the STATIC_ROOT setting.


6. [OPTIONAL] Add sponsors urls into your project's urls.py file::

    (r'^sponsors/', include('sponsors.urls')),

This will give url access to sponsors' views, not many in the very firsts versions :-(


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
