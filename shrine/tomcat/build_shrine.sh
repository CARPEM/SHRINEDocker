chmod +x $SECRETS
source $SECRETS

cp lib/shrine.conf.orig lib/shrine.conf

echo 'Configuring shrine'

echo 'shrine.conf'
###########################
#
#	Shrine.conf
#
sed -i "s#<NODE_NAME>#$NODE_NAME#g" lib/shrine.conf

#PM endpoint
sed -i "s#<PM_HOST>#$PM_HOST#g" lib/shrine.conf
sed -i "s#<PM_PORT>#$PM_PORT#g" lib/shrine.conf

#ont Enpoint
sed -i "s#<ONT_HOST>#$ONT_HOST#g" lib/shrine.conf
sed -i "s#<ONT_PORT>#$ONT_PORT#g" lib/shrine.conf

#crc Enpoint
sed -i "s#<CRC_HOST>#$CRC_HOST#g" lib/shrine.conf
sed -i "s#<CRC_PORT>#$CRC_PORT#g" lib/shrine.conf

#Hive credentials
sed -i "s#<I2B2_DOMAIN>#$I2B2_DOMAIN#g" lib/shrine.conf
sed -i "s#<SHRINE_CRC_USER>#$SHRINE_CRC_USER#g" lib/shrine.conf
sed -i "s#<SHRINE_CRC_PASSWORD>#$SHRINE_CRC_PASSWORD#g" lib/shrine.conf
sed -i "s#<I2B2_CRC_PROJECT_ID>#$I2B2_CRC_PROJECT_ID#g" lib/shrine.conf
sed -i "s#<SHRINE_ONT_PROJECT_ID>#$SHRINE_ONT_PROJECT_ID#g" lib/shrine.conf



#steward
sed -i "s#<QEP_USER>#$QEP_USER#g" lib/shrine.conf
sed -i "s#<QEP_PASSWORD>#$QEP_PASSWORD#g" lib/shrine.conf
sed -i "s#<SHRINE_WEBCLIENT_HOST>#$SHRINE_WEBCLIENT_HOST#g" lib/shrine.conf
sed -i "s#<SHRINE_WEBCLIENT_PORT>#$SHRINE_WEBCLIENT_PORT#g" lib/shrine.conf
sed -i "s#<SHRINE_HOST>#$SHRINE_HOST#g" lib/shrine.conf
sed -i "s#<SHRINE_PORT>#$SHRINE_PORT#g" lib/shrine.conf

#broadcaster
if [ "$IS_HUB" = "true" ]; then
	sed -i "s#<SHRINE_HUB_HOST>#shrine#g" lib/shrine.conf
	echo 'is HUB ==> TRUE'
else
	sed -i "s#<SHRINE_HUB_HOST>#$SHRINE_HUB_HOST#g" lib/shrine.conf
	echo 'is HUB ==> FALSE'
fi
sed -i "s#<SHRINE_HUB_PORT>#$SHRINE_HUB_PORT#g" lib/shrine.conf

#HUB

if [ "$IS_HUB" = "true" ]; then
	sed -i "s#<HUB>#  hub {\n	create = true\n	maxQueryWaitTime{\n		minutes = 5\n	}\n	downstreamNodes{\n		}\n		shouldQuerySelf=true\n	}#g" lib/shrine.conf
	echo 'is HUB ==> TRUE'
else
	sed -i "s#<HUB>#  hub {\n	create = false\n	}#g" lib/shrine.conf
	echo 'is HUB ==> FALSE'
fi

#keystore
sed -i "s#<KEYSTORE_FILE>#$KEYSTORE_FILE#g" lib/shrine.conf
sed -i "s#<KEYSTORE_PASSWORD>#$KEYSTORE_PASSWORD#g" lib/shrine.conf
sed -i "s#<KEYSTORE_ALIAS>#$KEYSTORE_ALIAS#g" lib/shrine.conf

echo 'context.xml'
######################
#
# CONTEXT.XML
#
cp conf/context.xml.orig conf/context.xml
sed -i "s#<SHRINE_DB_HOST>#$SHRINE_DB_HOST#g" conf/context.xml
sed -i "s#<SHRINE_DB_PORT>#$SHRINE_DB_PORT#g" conf/context.xml
sed -i "s#<MYSQL_USER>#$MYSQL_USER#g" 	conf/context.xml
sed -i "s#<MYSQL_PASSWORD>#$MYSQL_PASSWORD#g" conf/context.xml

echo 'server.xml'
######################
#
# SERVER.XML
#
cp conf/server.xml.orig conf/server.xml
sed -i "s#<KEYSTORE_FILE>#$KEYSTORE_FILE#g" conf/server.xml
sed -i "s#<KEYSTORE_PASSWORD>#$KEYSTORE_PASSWORD#g" conf/server.xml
sed -i "s#<KEYSTORE_ALIAS>#${KEYSTORE_ALIAS}_https#g" conf/server.xml
sed -i "s#<SHRINE_PORT>#$SHRINE_PORT#g" conf/server.xml
sed -i "s#<SHRINE_HOST>#$SHRINE_HOST#g" conf/server.xml

###################
#
#	WEBCLIENT
#

cp webapps/shrine-webclient/i2b2_config_data.js.orig webapps/shrine-webclient/i2b2_config_data.js
sed -i "s#<PM_HOST>#$PM_HOST#g" webapps/shrine-webclient/i2b2_config_data.js
sed -i "s#<PM_PORT>#$PM_PORT#g" webapps/shrine-webclient/i2b2_config_data.js


cp webapps/shrine-webclient/js-i2b2/cells/SHRINE/cell_config_data.js.orig webapps/shrine-webclient/js-i2b2/cells/SHRINE/cell_config_data.js
sed -i "s#<SHRINE_WEBCLIENT_HOST>#$SHRINE_WEBCLIENT_HOST#g" webapps/shrine-webclient/js-i2b2/cells/SHRINE/cell_config_data.js
sed -i "s#<SHRINE_WEBCLIENT_PORT>#$SHRINE_WEBCLIENT_PORT#g" webapps/shrine-webclient/js-i2b2/cells/SHRINE/cell_config_data.js

cd /opt/shrine
keytool -genkeypair -keysize 2048 -alias $KEYSTORE_ALIAS -dname "CN=$KEYSTORE_ALIAS, OU=$KEYSTORE_HUMAN, O=SHRINE Network, L=$KEYSTORE_CITY, S=$KEYSTORE_STATE, C=$KEYSTORE_COUNTRY" -keyalg RSA -keypass $KEYSTORE_PASSWORD -storepass $KEYSTORE_PASSWORD -keystore $KEYSTORE_FILE -storetype pkcs12 -validity 7300
keytool -certreq -alias $KEYSTORE_ALIAS -keyalg RSA -file $KEYSTORE_ALIAS.csr -keypass $KEYSTORE_PASSWORD -storepass $KEYSTORE_PASSWORD -keystore $KEYSTORE_FILE -ext SAN=dns:$KEYSTORE_ALIAS,dns:shrine
keytool -genkeypair -keysize 2048 -alias ${KEYSTORE_ALIAS}_https -dname "CN=$KEYSTORE_ALIAS, OU=HTTPS CA, O=SHRINE Network, L=$KEYSTORE_CITY, S=$KEYSTORE_STATE, C=$KEYSTORE_COUNTRY" -keyalg RSA -keypass $KEYSTORE_PASSWORD -storepass $KEYSTORE_PASSWORD -keystore $KEYSTORE_FILE -storetype pkcs12 -validity 7300 -ext SAN=dns:$KEYSTORE_ALIAS,dns:shrine
keytool -export -alias ${KEYSTORE_ALIAS}_https -storepass $KEYSTORE_PASSWORD -file ${KEYSTORE_ALIAS}_HTTPS.cer -keystore $KEYSTORE_FILE
keytool -import -v -trustcacerts -alias shrine-hub-ca -file ${KEYSTORE_ALIAS}_HTTPS.cer -keystore $KEYSTORE_FILE -storepass $KEYSTORE_PASSWORD -noprompt
#keytool -genkeypair -keysize 2048 -alias shrine -dname "CN=shrine, OU=shrine local, O=SHRINE Network, L=$KEYSTORE_CITY, S=$KEYSTORE_STATE, C=$KEYSTORE_COUNTRY" -keyalg RSA -keypass $KEYSTORE_PASSWORD -storepass $KEYSTORE_PASSWORD -keystore $KEYSTORE_FILE -storetype pkcs12 -validity 7300
keytool -list -v -keystore  $KEYSTORE_FILE -storepass $KEYSTORE_PASSWORD

cp ${KEYSTORE_ALIAS}_HTTPS.cer /opt/cert
cp $KEYSTORE_ALIAS.csr /opt/cert

sed -i "s#false#true#g" /opt/shrine/deployed
