#!/bin/bash

source $SECRETS
export VAR
VAR=${1#/opt/cert/}

if [ "$2" = "" ]; then
  NODE_NAME="unknown"
else
  NODE_NAME=$2
fi

echo "node domain ==> $VAR "
echo "node name ==> $NODE_NAME "
cp /opt/cert/${VAR}.csr /opt/shrine/newreq.pem
cd /opt/shrine
/usr/lib/ssl/misc/CA.pl -sign
mv /opt/shrine/newcert.pem /opt/cert/${VAR}-signed.crt
keytool  -import -v -alias ${VAR} -file /opt/cert/${VAR}_HTTPS.cer -keystore shrine.keystore -storepass $KEYSTORE_PASSWORD
if [ "$VAR" != "shrinelocal" ] ; then
  sed -i "s#\".*\" = \"https://${VAR}:6443/shrine/rest/adapter/requests\".*\n##g" tomcat/lib/shrine.conf
  sed -i "s#downstreamNodes{#downstreamNodes{\n \"$NODE_NAME\" = \"https://${VAR}:6443/shrine/rest/adapter/requests\"#g" tomcat/lib/shrine.conf
fi
