Slender Node Adapter Supporting schema.org described Resources
==============================================================

Notes for implementation of a "slender node" adapter to support synchronization
of content described with schema.org constructs.

Commandline executables
-----------------------

The following commandline utilities are included in this package and require Python 3.7.

* d1-validate - validates a single XML document against DataOne-supported formats
* d1-check-site - validate XML documents located through a sitemap URL
* harvest-adbs-ipt - harvest XML documents from the Arctic Biodiversity Data Service IPT RSS feed
* harvest-arm - harvest XML documents from the ARM Climate Research Faciility
* harvest-cuahsi - harvest XML documents from CUAHSI's Hydroshare online collaboration environment
* harvest-ieda - harvest XML documents from the Interdisciplinary Earth Data Alliance (IEDA) 
* harvest-nkn - harvest XML documents from the Northwest Knowledge Network (University of Idaho)

Install the utilities as follows:
```
$ python setup.py develop
```

In each case, the harvesters all have a similar commandline interface.  For example, ``harvest-arm`` has the following help:

```
usage: harvest-arm [-h] [-v {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [--host HOST]
                   [--port PORT] [--certificate CERTIFICATE]
                   [--private-key PRIVATE_KEY] [--num-documents NUM_DOCUMENTS]
                   [--regex REGEX] [--num-workers NUM_WORKERS]
                   [--max-num-errors MAX_NUM_ERRORS] [--ignore-harvest-time]
                   [--retry RETRY]

Harvest metadata from ARM.

optional arguments:
  -h, --help            show this help message and exit
  -v {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --verbosity {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Verbosity level of log file arm.log (default: INFO)
  --host HOST           Harvest records to this DataOne member node. (default:
                        localhost)
  --port PORT           DataOne member node SSL port. (default: 443)
  --certificate CERTIFICATE
                        Path to dataone client-side certificate. (default:
                        None)
  --private-key PRIVATE_KEY
                        Path to dataone host client-side key. (default: None)
  --num-documents NUM_DOCUMENTS
                        Limit number of documents retrieved to this number.
                        (default: -1)
  --regex REGEX         Limit documents retrieved to those whose URL match
                        this regular expression. (default: None)
  --num-workers NUM_WORKERS
                        Limit number of workers operating asynchronously to
                        this number. (default: 1)
  --max-num-errors MAX_NUM_ERRORS
                        Limit number of errors to this number. This number is
                        not exact, because if the number of asynchronous
                        workers is more than one, it is possible that the
                        threshold is passed simultaneously by more than one
                        worker. (default: 1)
  --ignore-harvest-time
                        Ignore the last harvest time. Use this switch to
                        attempt to harvest records that may have failed for
                        some reason on a recent harvest attempt. (default:
                        False)
  --retry RETRY         Retry a failed record this number of times. (default:
                        1)

Not supplying an argument to both the certificate and key arguments will
disable client side authentication.
```

Example URLs for d1-check-site
------------------------------
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

8. Two documents listed, but the first document does not validate according to any supported format IDs, which is different than having invalid XML.

    $ d1-check-site http://104.236.112.76/demo/metadata-document-does-not-validate/sitemap.xml

9. The sitemap is gzipped.

    $ d1-check-site http://104.236.112.76/demo/sitemap-is-gzipped/sitemap.xml.gz

10. The sitemap file is actually a sitemap index file, meaning there are multiple levels of sitemaps.

    $ d1-check-site http://104.236.112.76/demo/sitemap-url-is-sitemap-index-file/sitemap_index_file.xml

11. The sitemap file is text instead of XML.

    $ d1-check-site http://104.236.112.76/demo/sitemap-is-not-xml/sitemap.txt

12. Check only 5 documents.

    $ d1-check-site --num-documents=5 https://www.archive.arm.gov/metadata/adc/sitemap.xml
