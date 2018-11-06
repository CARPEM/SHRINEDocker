#!/bin/bash

source $SECRETS
/usr/lib/ssl/misc/CA.pl -newca
cp demoCA/cacert.pem /opt/cert/shrine-hub-ca.crt
cp /opt/cert/${SHRINE_HOST}.csr /opt/shrine/newreq.pem
cd /opt/shrine
/usr/lib/ssl/misc/CA.pl -sign
mv /opt/shrine/newcert.pem /opt/cert/${SHRINE_HOST}-signed.crt
cp /opt/cert/${KEYSTORE_ALIAS}_HTTPS.cer /opt/cert/shrine-hub-https-ca.crt

keytool -delete -v -alias shrine-hub-ca -keystore shrine.keystore -storepass $KEYSTORE_PASSWORD
keytool -import -v -alias shrine-hub-ca -file /opt/cert/shrine-hub-ca.crt -keystore shrine.keystore -storepass $KEYSTORE_PASSWORD
keytool -import -v -alias shrine-hub-https-ca -file /opt/cert/shrine-hub-https-ca.crt -keystore shrine.keystore -storepass $KEYSTORE_PASSWORD
keytool -import -v -alias $KEYSTORE_ALIAS -file /opt/cert/${KEYSTORE_ALIAS}-signed.crt -keystore shrine.keystore -storepass $KEYSTORE_PASSWORD -keypass $KEYSTORE_PASSWORD -trustcacerts
keytool -import -list -v -keystore shrine.keystore -storepass $KEYSTORE_PASSWORD
