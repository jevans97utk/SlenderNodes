Create the GMN client side certificate
=======================================

The PASTA-GMN Adapter connects over TLS/SSL to GMN, using a client side
certificate that is signed by a local CA, trusted by GMN.

A local CA is created and set up to be trusted by GMN as a standard step in the
GMN installation, so all that remains to be done here is to create an additional
client side certificate for the Adapter that is signed by the same CA.

The DN in the certificate becomes the submitter and rights holder for the
DataONE representations of the PASTA packages.

What follows is the procedure for creating the certificate. For more background
information, see the page about client side certificates in the GMN
documentation.

When prompted for the Common Name, it is suggested that "PASTA-GMN" is used
(without the quotes).

The CA password is the one that was set when the CA was created as part of the
GMN installation.

::

  $ cd /var/local/dataone/certs/local_ca

  $ openssl req -config ./openssl.cnf -new -newkey rsa:2048 -nodes \
  -keyout private/pasta_gmn_key.pem -out pasta_gmn_csr.pem

  $ sudo openssl rsa -in private/pasta_gmn_key.pem -out private/pasta_gmn_key_nopassword.pem

  $ sudo openssl rsa -in private/pasta_gmn_key_nopassword.pem -pubout -out pasta_gmn_public_key.pem

  $ sudo openssl ca -config ./openssl.cnf -in pasta_gmn_csr.pem -out pasta_gmn_cert.pem

  $ sudo rm pasta_gmn_csr.pem


Other names may be used. If so, update the `CLIENT_CERT_PATH` and
`CLIENT_CERT_PRIVATE_KEY_PATH` settings in the PASTA-GMN Adapter ``settings.py``
file to match the new names.
