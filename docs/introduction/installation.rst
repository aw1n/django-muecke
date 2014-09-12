.. index:: Installation

============
Installation
============

Prerequisites
=============

Make sure you have installed:

* Python 2.6.x or 2.7.x
* A RDBMS of your choice (PostgreSQL, MySQL, SQLite or Oracle)

Installation
============

The installation is straightforward and should last just a few minutes. Please
execute following steps:

#. Download the installer from http://pypi.python.org/pypi/django-muecke

#. $ tar xzf django-muecke-installer-<version>.tar.gz

#. $ cd muecke-installer

#. $ python bootstrap.py

#. $ bin/buildout -v

#. Enter your database settings to muecke_project/settings.py

#. $ bin/django syncdb

#. $ bin/django muecke_init

#. $ bin/django collectstatic

#. $ bin/django runserver

#. Browse to http://localhost:8000/

Migration
=========

Starting with version 0.6 we provide a migration command (``muecke_migrate``)
which migrates existing databases to the latest release.

To migrate an existing database please proceed the following steps:

#. Install the new version (see above)

#. Backup your existing database

#. Enter your existing database to muecke_project/settings.py

#. $ bin/django syncdb

#. $ bin/django muecke_migrate

After that your database should be ready to run with the latest release.

What's next?
============
Move on to :doc:`getting_started`.
