OAI-PMH Slender Node Adapter for GMN
====================================

The Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH_) is a widely used protocol that enables retrieval of metadata from repositories. There are many parallels between this protocol and the DataONE Member Node API for read only access, though falls short on a couple key criteria.

1. OAI-PMH is, as the name suggestes, for metadata harvest rather than a generic object retrieval protocol.

2. There is no access control inherent in the protocol, leading to no access control or varying implementations across repositories.

The goal of this adapapter implementation is to enable support of the DataONE Member Node APIs to allow Tier 1 access to metadata, with a recommendation for exposing data through Member Node service registration metadata records.


.. _OAI-PMH: http://www.openarchives.org/pmh/


Test Case - PANGAEA
-------------------

The PANGAEA_ repository is a good test case as it provides an implementation of an OAI-PMH service and also provides access to data through a service interface. 

Services offered by PANGAEA include:

* OAI-PMH
* Elasticsearch 
* "Value added" services for parameterized data download
* Proprietary search and background services described in WSDL

OAI-PMH provides the basic mechanisms for discovering content and retrieving the metadata for that content. OAI-PMH is a widely deployed protocol, and support for this by an adapter to and existing Member Node implementation may result in a solution that could be widely deployed.

Some useful URLs for PANGAEA include:

* PANGAEA website:  https://www.pangaea.de/
* PANGAEA service listing: https://ws.pangaea.de/
* PANGAEA OAI-PMH description: https://ws.pangaea.de/oai/
* PANGAEA OAI-PMH endpoint: https://ws.pangaea.de/oai/provider


.. _PANGAEA: https://www.pangaea.de/


Design
------

The adapter will retrieve metadata from the OAI-PMH endpoint, generate system metadata for the content and make the content available to DataONE through the GMN API.


Retrieving a List of New of Changed Entries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


OAI-PMH has a couple methods to support introspection, in particular

* ListIdentifiers: http://www.openarchives.org/OAI/openarchivesprotocol.html#ListIdentifiers

* ListRecords: http://www.openarchives.org/OAI/openarchivesprotocol.html#ListRecords


Both methods support time slicing with option ``from`` and ``until`` arguments which accept a UTC date time value. 

Both methods have a required argument ``metadataPrefix``, valid values for which may be determined from the ListMetadataFormats_ method.

OAI-PMH method ``ListIdentifiers`` example output::

  curl -s "https://ws.pangaea.de/oai/provider?verb=ListIdentifiers&metadataPrefix=iso19139" | xml fo
  
  <?xml version="1.0" encoding="UTF-8"?>
  <?xml-stylesheet type="text/xsl" href="oai2.xsl"?>
  <OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/
                               http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
    <responseDate>2017-03-13T17:17:28Z</responseDate>
    <request verb="ListIdentifiers"
       metadataPrefix="iso19139">https://ws.pangaea.de/oai/provider</request>
    <ListIdentifiers>
      <header>
        <identifier>oai:pangaea.de:doi:10.1594/PANGAEA.51463</identifier>
        <datestamp>2017-02-15T14:26:54Z</datestamp>
        <setSpec>citable</setSpec>
        <setSpec>citableWithChilds</setSpec>
        <setSpec>supplement</setSpec>
      </header>
      <header>
        <identifier>oai:pangaea.de:doi:10.1594/PANGAEA.51481</identifier>
        <datestamp>2016-12-13T11:02:35Z</datestamp>
        <setSpec>citable</setSpec>
        <setSpec>citableWithChilds</setSpec>
        <setSpec>supplement</setSpec>
      </header>
      <header>
        <identifier>oai:pangaea.de:doi:10.1594/PANGAEA.51506</identifier>
        <datestamp>2017-02-15T14:55:18Z</datestamp>
        <setSpec>citable</setSpec>
        <setSpec>citableWithChilds</setSpec>
        <setSpec>supplement</setSpec>
      </header>

  ...

      <header>
        <identifier>oai:pangaea.de:doi:10.1594/PANGAEA.774044</identifier>
        <datestamp>2017-03-05T13:44:52Z</datestamp>
        <setSpec>citable</setSpec>
        <setSpec>citableWithChilds</setSpec>
        <setSpec>supplement</setSpec>
      </header>
      <resumptionToken expirationDate="2017-03-13T17:29:24Z"
               cursor="0">d3cf2b7a-966a-49e0-8af1-cfd75fa5a6fb</resumptionToken>
    </ListIdentifiers>
  </OAI-PMH>


OAI-PMH method ``ListRecords`` example output from PANGAEA::

  <?xml version="1.0" encoding="UTF-8"?>
  <?xml-stylesheet type="text/xsl" href="oai2.xsl"?>
  <OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ 
                               http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
    <responseDate>2017-03-13T17:20:32Z</responseDate>
    <request verb="ListRecords" metadataPrefix="iso19139">https://ws.pangaea.de/oai/provider</request>
    <ListRecords>
      <record>
        <header>
          <identifier>oai:pangaea.de:doi:10.1594/PANGAEA.51463</identifier>
          <datestamp>2017-02-15T14:26:54Z</datestamp>
          <setSpec>citable</setSpec>
          <setSpec>citableWithChilds</setSpec>
          <setSpec>supplement</setSpec>
        </header>
        <metadata>
          <MD_Metadata xmlns:xlink="http://www.w3.org/1999/xlink"
                       xmlns:gmd="http://www.isotc211.org/2005/gmd"
                       xmlns:gco="http://www.isotc211.org/2005/gco"
                       xmlns:gml="http://www.opengis.net/gml"
                       xmlns="http://www.isotc211.org/2005/gmd"
                       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                       xsi:schemaLocation="http://www.isotc211.org/2005/gmd
                                     http://www.isotc211.org/2005/gmd/gmd.xsd"
                       id="de.pangaea.dataset51463">
            <fileIdentifier>
              <gco:CharacterString>de.pangaea.dataset51463</gco:CharacterString>
            </fileIdentifier>
            <contact>
  ...

                </lineage>
              </DQ_DataQuality>
            </dataQualityInfo>
          </MD_Metadata>
        </metadata>
      </record>
      <resumptionToken expirationDate="2017-03-13T17:31:02Z"
              cursor="0">2e0424e8-6dad-4bf2-ad02-ffda4a60f217</resumptionToken>
    </ListRecords>
  </OAI-PMH>


.. _ListMetadataFormats: http://www.openarchives.org/OAI/openarchivesprotocol.html#ListMetadataFormats

Retrieving Bytes of an Entry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Retrieving the bytes of metadata is straightforward with the OAI-PMH service interface. The general approach may be something like the following pseudo code::

  identifiers = OAIPMH.ListIdentifiers(start_date, now)
  for identifier in identifiers:
    metadata = OAIPMH.GetRecord(identifier)
    sysmeta = generateSystemMetadata(metadata)
    MemberNode.CreateOrUpdate(identifier, sysmeta, metadata)



Other Resources
---------------

* OAI-PMH specification: http://www.openarchives.org/pmh/
* pyoai library: https://pypi.python.org/pypi/pyoai
* Python oaiharvest tool and lib: https://github.com/bloomonkey/oai-harvest
