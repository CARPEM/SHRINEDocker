#!/bin/bash

source $SECRETS
export VAR
VAR=${1#/opt/cert/}
echo $VAR
cp /opt/cert/${VAR}.csr /opt/shrine/newreq.pem
cd /opt/shrine
/usr/lib/ssl/misc/CA.pl -sign
mv /opt/shrine/newcert.pem /opt/cert/${VAR}-signed.crt
keytool  -import -v -alias ${VAR} -file /opt/cert/${VAR}_HTTPS.cer -keystore shrine.keystore -storepass $KEYSTORE_PASSWORD
sed -i "s#downstreamNodes{#downstreamNodes{\n           \"$2\" = \"https://${VAR}:6443/shrine/rest/adapter/requests\"#g" tomcat/lib/shrine.conf
