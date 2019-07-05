Slender Node Adapter Supporting schema.org described Resources
==============================================================

Notes for implementation of a "slender node" adapter to support synchronization
of content described with schema.org constructs.

Examples: d1-check-site
-----------------------
Before anything else, you need to do an install a new command line utility
called d1-check-site.

```
$ python setup.py develop
```

1. No sitemap.

    $ d1-check-site http://104.236.112.76/demo/no_site_map/sitemap.xml

2. Two documents listed in sitemap, but one landing page is missing.

    $ d1-check-site http://104.236.112.76/demo/no_landing_page/sitemap.xml

3. A landing page has invalid JSON-LD.

    $ d1-check-site http://104.236.112.76/demo/invalid-json-ld/sitemap.xml

4. A landing page is missing its JSON-LD SCRIPT element.

    $ d1-check-site http://104.236.112.76/demo/missing-json-ld-script-element/sitemap.xml

5. A landing page is missing its JSON-LD ID.

    $ d1-check-site http://104.236.112.76/demo/missing-json-ld-id/sitemap.xml

6. Two documents listed, but one metadata XML document is missing.

    $ d1-check-site http://104.236.112.76/demo/missing-metadata-document/sitemap.xml

7. Two documents listed, but one metadata XML document has invalid XML.

    $ d1-check-site http://104.236.112.76/demo/metadata-document-has-invalid-xml/sitemap.xml

8. Two documents listed, but the first document does not validate, which is different than having invalid XML.

    $ d1-check-site http://104.236.112.76/demo/metadata-document-does-not-validate/sitemap.xml

9. The sitemap is gzipped.

    $ d1-check-site http://104.236.112.76/demo/sitemap-is-gzipped/sitemap.xml.gz

10. The sitemap file is actually a sitemap index file, meaning there are multiple levels of sitemaps.

    $ d1-check-site http://104.236.112.76/demo/sitemap-url-is-sitemap-index-file/sitemap_index_file.xml

11. The sitemap file is text instead of XML.

    $ d1-check-site http://104.236.112.76/demo/sitemap-is-not-xml/sitemap.txt

TLDR;
-----
```
$ python setup.py install
```

This will install two command-line utilities, harvest-ieda and harvest-arm, that may be used to harvest IEDA and ARM metadata.

```
$ harvest-ieda -h
usage: harvest-ieda [-h] [-v {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                [--host HOST] [--port PORT] [--certificate CERTIFICATE]
                [--key KEY]

Harvest metadata from IEDA.

optional arguments:
  -h, --help            show this help message and exit
  -v {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --verbose {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Verbosity level of log file ieda.log (default: INFO)
  --host HOST           Harvest records to this dataone node host. This is NOT
                        the host where the site map is found. (default:
                        localhost)
  --port PORT           DataONE host SSL port. (default: 443)
  --certificate CERTIFICATE
                        Path to dataone host certificate. (default: None)
  --key KEY             Path to dataone host private key. (default: None)

Not supplying an argument to both the certificate and key arguments will
disable client side authentication.
```


Discovery Pattern
-----------------

The general pattern for discovery of schema.org resources given a domain name is:

1. parse http(s)://domain.name/robots.txt

   This step is optional if the location of the sitemap.xml is known (step 2)

2. Get the sitemap.xml file from the location identified or inferred from robots.txt

3. For each entry in the sitemap.xml file:

   a. Parse the resource and extract the schema.org information

   b. If sufficient and appropriate schema.org information is available, then add the
      referenced resource or resources to the set of items to be processed. Note that
      the sitemap.xml may point to Dataset or a DataCatalog instance. In the latter case,
      the DataCatalog item should be processed to discover the contained Dataset
      instances.

A schema.org Dataset instance is considered to be the target item for synchronization by
DataONE, and the Dataset should contain references to the components of the Dataset.

DataONE treats the Dataset instance as a view of the actual dataset, with parts of the
view populated from difference components of the dataset such as the metadata and
resource map or its equivalent providing relationships between components.


Dataset Constructs
------------------

This content is in DRAFT status, subject to change.

Required properties:

* identifier
* datePublished
* dateModified  (required if there are updates after datePublished)
* distribution

The distribution element must be an array of DataDownload entries, one for each component
of the dataset being desribed.

Each entry in distribution should include:

* identifier
* encodingFormat
* name
* url
* "additionalType": "http://www.w3.org/ns/dcat#DataCatalog"



