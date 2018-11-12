#!/bin/bash
source $SECRETS

keytool -delete -v -alias shrine-hub-ca -keystore shrine.keystore -storepass $KEYSTORE_PASSWORD
keytool -import -v -alias shrine-hub-ca -file /opt/cert/shrine-hub-ca.crt -keystore shrine.keystore -storepass $KEYSTORE_PASSWORD
keytool -import -v -alias shrine-hub-https-ca -file /opt/cert/shrine-hub-https-ca.crt -keystore shrine.keystore -storepass $KEYSTORE_PASSWORD
keytool -import -v -alias $KEYSTORE_ALIAS -file /opt/cert/${KEYSTORE_ALIAS}-signed.crt -keystore shrine.keystore -storepass $KEYSTORE_PASSWORD -keypass $KEYSTORE_PASSWORD -trustcacerts
keytool -import -list -v -keystore shrine.keystore -storepass $KEYSTORE_PASSWORD
./logKeystore.sh
