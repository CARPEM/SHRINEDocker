#!/bin/bash

source $SECRETS

unzip /opt/i2b2webclient-1710.zip -d /opt/tempWebclient/
set WEBCLIENT_DIR =
echo $(ls -d /opt/tempWebclient/*/)
mv  $(ls -d /opt/tempWebclient/*/)/ /var/www/html/webclient/

sed -i "s#name:.*#name:\"test\",#g" /var/www/html/webclient/i2b2_config_data.js
sed -i "s#urlCellPM:.*#urlCellPM:\"http://$I2B2_HOST:$I2B2_PORT/i2b2/services/PMService/\",#g" /var/www/html/webclient/i2b2_config_data.js
sed -i "s#\"http://localhost:9090\",.*#\"http://localhost:9090\",\"http://$I2B2_HOST:$I2B2_PORT\",#g" /var/www/html/webclient/index.php


sed -i "s#false#true#g" deployed
