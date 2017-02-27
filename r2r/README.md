## DataONE R2R SlenderNode Connector for GMN

The R2R SlenderNode Connector is a Python script that periodically checks the [The Rolling Deck to Repository (R2R)](http://www.rvdata.us/) for new and updated metadata records using the [R2R Web Services](http://api.rvdata.us/). When new and updated records are discovered, the connector exposes them to [DataONE](dataone.org) by creating Science Objects on a local instance of the [DataONE Generic Member Node (GMN)](http://pythonhosted.org/dataone.generic_member_node/). 

### Install

For ease of deployment, the connector is designed to share GMN's virtual environment and requires no dependencies beyond those installed as part of GMN. So this procedure describes how to deploy the connector side by side with an operational instance of GMN.
 
* Go to the root of the GMN install and become the gmn user.

```sh
$ cd /var/local/dataone
$ sudo su gmn
```
    
* Get the connector directly from GitHub.

```sh
$ git clone <copy and paste the "Clone with HTTPS" URL from the top of this page> 
```

* Edit the settings as required in the script.
 
```sh
$ nano SlenderNodes/r2r/r2r_connecter.py
```

* Add a cron job for the script.

```sh
$ crontab -e
10 * * * * cd /var/local/dataone/SlenderNodes/r2r && /var/local/dataone/gmn/bin/python ./r2r_connector.py >> r2r.log 2>&1
```

### Operation

The connector queries the R2R Web Services for metadata records using the query:

```sh
http://api.rvdata.us/catalog?service=CSW&version=3.0.0&request=GetRecords&typenames=gmd:MD_Metadata&outputSchema=http://www.isotc211.org/2005/gmd&elementSetName=full
```

It uses the `maxRecords` and `startPosition` query parameters to process the results one page at a time. Each page is first parsed to an ElementTree. Then, in the ET domain, it iterates over the metadata records in the page. Each metadata record is serialized to a new XML doc where the metadata record starts at the root. The new XML doc is then hashed with SHA-1 and the hash is used as the PID.

The connector then queries GMN for the PID and if it exists, the object has already been created and the connector just moves on to the next record.

If the PID doesn't exist, the connector tries to resolve the SID (which is the gmd:fileIdentifier). If the SID doesn't resolve, it's a brand new record and the connector does a create() and registers the SID. If the SID does resolve, it's a modified record, and the connector does an update(), obsoleting the PID that the SID resolved to, and updating the SID to point to the new PID.
