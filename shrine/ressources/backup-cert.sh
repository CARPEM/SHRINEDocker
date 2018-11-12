#!/bin/bash
source $SECRETS

cp /opt/shrine/shrine.keystore /opt/cert/shrine.keystore.bkp
keytool -list -v -keystore shrine.keystore -storepass $KEYSTORE_PASSWORD
