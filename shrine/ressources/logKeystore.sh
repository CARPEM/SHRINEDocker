#!/bin/bash
source $SECRETS


echo '**************************************************************************************' >> /op/cert/keystoreList.txt
keytool -import -list -v -keystore shrine.keystore -storepass $KEYSTORE_PASSWORD >> /op/cert/keystoreList.txt
