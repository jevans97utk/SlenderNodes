Implementation notes
====================

Pure SQL
~~~~~~~~

This web app is different from most Django applications in that it does not
use the Django ORM. Instead it uses pure SQL. Because of this, there is no
models.py file.

The database is created with the command line in :doc:`setup-final`.


PASTA API Wrapper
~~~~~~~~~~~~~~~~~

This project includes a Python wrapper for the PASTA API that may be usable
as a library for other Python applications. The library is implemented in:

/var/local/dataone/pasta_gmn_adapter/adapter/management/commands/data_package_manager_client.py


For testing, a new package can be manually added to the queue with::

  $ curl -i --data "knb-lter-nin.6.1" http://127.0.0.1


Unit tests
~~~~~~~~~~

To run the unit tests::

  ./manage.py test



Cardinality of a PASTA data package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Metadata: 1
- Quality report: 1
- Data entities: 1 to many

In addition to this, one OAI-ORE Resource Map is added to GMN for each PASTA
package.


DOIs
~~~~

PASTA registers DOIs asynchronously. So DOIs may not be ready when PASTA
registers the package with the Adapter for export to GMN. This is resolved by
automatically retrying packages that fail due to missing data at a later time.


Package updates
~~~~~~~~~~~~~~~

New revisions of the same PASTA packages (same scope and identifiers but
different revision) are created as updates to the latest existing package. In a
new revision of the package, the number of data entities may change and there is
no automatic way to determine the relationship between data entities in the new
revision and the existing one. Due to this, only the OAI-ORE Resource Map for
the package is created as an update to the existing package. The other objects
in the package are created as new objects.


Handling of private packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Processing is aborted on any package if one or more of its components are found
to not be publicly accessible. The package is then marked as private and the
Adapter will not attempt to process the package again.
