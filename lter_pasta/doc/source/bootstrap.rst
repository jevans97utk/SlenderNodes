Register existing packages
==========================

When the PASTA-GMN Adapter is started, it will process all new packages going
forward. The following procedure registers the existing packages with
the Adapter so that they can be processed before the new packages.

It is important that the existing packages be processed first because the
Adapter uses MNStorage.create() and MNStorage.update() calls in order to create
a correct chain of obsolescence on GMN. The Adapter will reject any package
from PASTA that is older than any related packages that have already been
populated into GMN.

To register the new packages:

Become the gmn user::

  $ sudo -s -u gmn

Activate the gmn virtualenv::

  $ . /var/local/dataone/gmn/bin/activate

Go to the PASTA-GMN Adapter home directory::

  $ cd /var/local/dataone/pasta_gmn_adapter

Run the script that populates the existing packages::

  $ ./populate_existing_packages.sh

This script simply runs two management commands and pipes the output to log
files. The first command, ``register_existing_packages``, iterates over all
existing packages in PASTA and adds them to the Adapter's population queue. The
second command, ``process_population_queue`` is not strictly necessary. It's the
same command that is executed periodically by cron to process the queue. When
the script has completed, PASTA's support for sending notifications when new
packages are registered enables new packages to be automatically processed going
forward.

