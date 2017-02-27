Configure PostgreSQL
====================

These settings assume that PostgreSQL has already been set up and configured for
GMN.

  Create a database for the PASTA-GMN Adapter::

    $ sudo -u postgres createdb -E UTF8 pasta_gmn_adapter
