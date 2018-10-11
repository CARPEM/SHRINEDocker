#!/bin/bash

source $SECRETS
/usr/lib/ssl/misc/CA.pl -newca
cp demoCA/cacert.pem /opt/cert/shrine-hub-ca.crt
cp /opt/cert/${SHRINE_HOST}.csr /opt/shrine/newreq.pem
cd /opt/shrine
/usr/lib/ssl/misc/CA.pl -sign
mv /opt/shrine/newcert.pem /opt/cert/${SHRINE_HOST}-signed.crt
./import-cert.sh
