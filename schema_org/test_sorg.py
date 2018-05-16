'''
Examine a schema.org resource provider

Script for messing around with schema.org resources, evaluating content exposed by IEDA

Notes:

Resources listed at: http://get.iedadata.org/sitemaps/

'''

import logging
import sys
import requests
from lxml import etree
from w3lib.html import get_base_url as getBaseUrl
from extruct.jsonld import JsonLdExtractor
import json
import re
import pprint

NAMESPACES = {"sm":"http://www.sitemaps.org/schemas/sitemap/0.9"}


HTML_OR_JS_COMMENTLINE = re.compile('^\s*(//.*|<!--.*-->)')

class ModifiedJsonLdExtractor(JsonLdExtractor):
  '''
  Add more diagnostic to the extruct json-ld extractor

  https://github.com/scrapinghub/extruct/blob/master/extruct/jsonld.py
  '''

  def dumpJsonError(self, script, error):
    line_no = 1
    for line in script.split("\n"):
      print("{}: {}".format(line_no, line))
      line_no += 1
    pprint.pprint(error)


  def cleanJsonDecodeError(self, script, error):
    logging.debug("Bad char ordinal = %s at position %d", ord(script[error.pos]), error.pos)
    cleaned = "{}{}".format(script[:error.pos],script[error.pos+1:])
    return cleaned


  def parseJson(self, script, max_tries = 50):
    '''
    Keep trying to parse the provided JSON, replacing bad chars in the text with each try.

    This was needed to parse most of the IEDA content which seems to be malformed.

    :param script: json text
    :param max_tries: maximum times to try fixing before giving up
    :return: parsed json or nothing
    '''
    n_tries = 0
    while n_tries < max_tries:
      try:
        n_tries += 1
        logging.debug("Parse json attempt %d", n_tries)
        data = json.loads(script)
        if n_tries > 1:
          logging.warning("Used %d attempts to fix json data!", n_tries)
        return data
      except json.decoder.JSONDecodeError as e:
        if n_tries >= max_tries:
          self.dumpJsonError(script, e)
          raise(e)
        script = self.cleanJsonDecodeError(script, e)
      except ValueError as e:
        script = HTML_OR_JS_COMMENTLINE.sub('', script)
    return None


  def _extract_items(self, node):
    script = node.xpath('string()')
    data = self.parseJson(script)
    if isinstance(data, list):
      return data
    elif isinstance(data, dict):
      return [data]


def loadResourcesFromSitemap(sitemap):
  '''

  :param sitemap: URL to sitemap XML document to process
  :return: list of {url:"", date_modified:""}
  '''
  resources = []
  sitemap_xml = etree.parse(sitemap)
  urls = sitemap_xml.xpath("//sm:urlset/sm:url", namespaces=NAMESPACES)
  logging.debug("Found %d entries in sitemap %s", len(urls), sitemap)
  for url in urls:
    resource = {
      "url": url.xpath("sm:loc", namespaces=NAMESPACES)[0].text,
      "date_modified": url.xpath("sm:lastmod", namespaces=NAMESPACES)[0].text,
    }
    resources.append(resource)
  return resources


def loadSchemaOrg(resource):
  '''
  Load schema.org information from a specified resource URL

  :param resource: URL
  :return: dictionary of values
  '''
  response = requests.get(resource["url"])
  data = []
  extractor = ModifiedJsonLdExtractor()
  try:
    data = extractor.extract( response.content )
  except json.decoder.JSONDecodeError as e:
    logging.error( e )
    return {"error": str(e) }
  if len(data) < 1:
    return {"error":"No json-ld in resource."}
  if len(data) > 1:
    logging.warning("More than one json-ld block found. Using #0.")
  if data[0]["@type"] == "Dataset":
    entry = {
      "id": data[0]["@id"].strip(),
      "metadata_url": None,
      "metadata_format": None,
    }
    for ddownload in data[0]["distribution"]:
      if ddownload["@type"] == "DataDownload":
        if ddownload["name"] == "ISO Metadata Document":
          entry["metadata_url"] = ddownload["url"].strip()
    return entry
  return {"error":"Not a Dataset resource."}


def main():
  logging.basicConfig(level=logging.INFO)
  sitemap = "http://get.iedadata.org/sitemaps/usap_sitemap.xml"
  resources = loadResourcesFromSitemap(sitemap)
  for resource in resources:
    sorg_info = loadSchemaOrg(resource)
    result = {**resource, **sorg_info}
    try:
      print("{date_modified}, {url}, {id}, {metadata_url}".format( **result ))
    except KeyError as e:
      print("{date_modified}, {url}, {error}".format(**result))
  return 0


if __name__ == "__main__":
  sys.exit(main())

