#!/bin/bash
source $SECRETS

cp /opt/cert/shrine.keystore.bkp /opt/shrine/shrine.keystore
keytool -import -list -v -keystore shrine.keystore -storepass $KEYSTORE_PASSWORD
./logKeystore.sh
