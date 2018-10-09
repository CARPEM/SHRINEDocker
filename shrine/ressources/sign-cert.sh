source $SECRETS
cp /opt/cert/${1}.csr /opt/shrine/newreq.pem
cd /opt/shrine
/usr/lib/ssl/misc/CA.pl -sign
mv /opt/shrine/newcert.pem /opt/cert/${1}-signed.crt
keytool  -import -v -alias ${1} -file /opt/cert/${1}_HTTPS.cer -keystore shrine.keystore -storepass $KEYSTORE_PASSWORD
