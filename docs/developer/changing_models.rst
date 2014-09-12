.. index:: Changing models

===============
Changing models
===============

This section describes how to modify and create new models in LFS

Overview
========

Since version 0.8 LFS uses `South <http://south.aeracode.org/>`_ migrations so you're encouraged to read South
documentation first. If you need to modify models layer of LFS then you should use 'shemamigration' command. If you
have to migrate data then you should use 'datamigration' command. See examples below.

.. note::

  Do not forget to commit migrations into repository! They're created in migrations/ directory of the application they're crated for

Examples
========

New field added to the model, or modified existing field in muecke.customer::

    $ bin/django schemamigration muecke.customer --auto

New model added to muecke.catalog::

    $ bin/django schemamigration muecke.customer --auto

Execute migration that was just created with 'schemamigration'::

    $ bin/django schemamigration muecke.customer --auto
    $ bin/django migrate muecke.customer

Correct migration instead of creating new one, eg. if you've created a migration and then realized that your model still
has to be corrected (see more `here <http://south.readthedocs.org/en/latest/tutorial/part3.html?highlight=update>`_)::

    $bin/django schemamigration muecke.customer --auto --update
