PASTA-GMN Overview
==================

:term:`PASTA-GMN` is a DataONE Member Node based on :term:`LTER PASTA` and
:term:`GMN`. The two systems are integrated via the :term:`PASTA-GMN Adapter`.

The PASTA-GMN Adapter receives a call from PASTA whenever a new data package is
added to PASTA. The call from PASTA contains the package scope, identifier and
version of the new package. The Adapter stores this information in a queue of
packages to be processed.

At regular intervals, an asynchronous process starts and processes all new
packages in the queue. When the Adapter processes a package it first makes
multiple calls to the PASTA REST interface and gathers information about the
package.

When all information has been successfully gathered, the Adapter creates a
DataONE representation of the package. The DataONE representation of the package
includes an OAI-ORE Resource Map and DataONE System Metadata for all the
objects.

The Adapter then makes a number of DataONE Member Node REST interface calls to
GMN to create the objects for the new package.

When the objects have been successfully created on GMN, the package is marked as
successfully processed in the Adapter's queue of packages.

The Adapter uses GMN's ability to stream data through from a 3rd party web
server to avoid storing a copy in GMN, of the data that is in PASTA.

When the objects in the package have been created in GMN, they become visible
to the :term:`CN` the next time GMN is synchronized.

When a client accesses the package objects through the DataONE interface, they
are either served directly from GMN's local store or they are streamed through
from PASTA by GMN. Resource Maps and System Metadata are served from GMN's local
store and data entities are streamed from PASTA.
