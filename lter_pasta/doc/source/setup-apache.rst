Configure Apache
================

These settings assume that Apache has already been set up and configured for
GMN.

  Install the PASTA-GMN Adapter virtual host file::

    $ cd /var/local/dataone/pasta_gmn_adapter/deployment
    $ sudo cp pasta-gmn-adapter.conf /etc/apache2/sites-available/

  Enable the PASTA-GMN Adapter virtual host::

    $ sudo a2ensite pasta-gmn-adapter
