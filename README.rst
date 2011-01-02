``django-smileys`` is an application that allows your Django-powered site to
display those annoying and useless smileys whenever the ``smileys`` filter a
pattern that you specify.  This application serves a very simple purpose, but
its uses can go beyond that of merely inserting smileys whenever a particular
pattern (like ":)" or ";)").  It can replace whatever pattern you want with an
image of your choosing.  There's gotta be something useful in that, right?

This application can make your blog, forums, photo galleries, user comments,
etc a little more interesting, and it's very simple to install.  Free icon sets
plague the Internet, and you can choose whatever icons you'd like to use!

Features
========

* Strict pattern matching: you can specify very strict patterns for your
  smileys
* Regular expression pattern matching: if you need a little more power in your
  pattern matching capabilities, you can specify that your patterns are regular
  expressions (on a per-smiley basis) and the filter should know what to do.

Requirements
============

This application was built on Django 1.0.2, and it should work with any version
of Django that uses the ``admin.site.register`` method for telling the Django
admin that a model should appear in the admin (as opposed to the ``class
Admin:`` method).

Installation
============

Download ``django-smileys`` using *one* of the following methods:

easy_install or pip
-------------------

You can download the package from the `CheeseShop
<http://pypi.python.org/pypi/django-smileys/>`_ or use one of the following
commands::

    easy_install django-smileys
    pip install -U django-smileys

to download and install ``django-smileys``.

Clone From Version Control
--------------------------

You can grab the latest copy of the source code by cloning the project from one
of these official repositories::

    hg clone http://bitbucket.org/codekoala/django-smileys
    git clone http://github.com/codekoala/django-smileys.git
    hg clone http://django-smileys.googlecode.com/hg django-smileys

Package Download
----------------

Download the latest ``.tar.gz`` file from the downloads section and extract it
somewhere you'll remember.

Configuration
=============

First of all, you must add this project to your list of ``INSTALLED_APPS`` in
``settings.py``::

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        ...
        'smileys',
        ...
    )

Run ``manage.py syncdb``.  This creates a the table in your database that is
necessary for operation.

Usage
=====

Open the template file that you want to have your smileys appear in and make
sure it has something like this in it::

    {% load smiley_tags %}

    {% block content %}
    {{ some_content_var|smileys }}
    {% endblock %}

The ``smiley_tags`` library provides you with a ``smileys`` filter, which will
examine your database for all active smileys.  It then runs though
``some_content_var`` (in this example) and replaces the patterns it finds with
the respective smileys.  More recent versions also contain a
``textile_smileys`` tag for users of Textile formatting.  Pretty simple huh!

And useless! w00t.
