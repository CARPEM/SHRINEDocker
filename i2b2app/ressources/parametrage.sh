#!/bin/bash/

chmod +x $SECRETS
source $SECRETS
ROOTDIRECTORY=$(dirname $(readlink -f "$0"))

#DEBUG
echo $ROOTDIRECTORY
echo "source file name ==> " $i2b2_SOURCE_FILE_NAME
cd $ROOTDIRECTORY



#rm jboss -R
#rm axis2-1.7.1-war.zip

#unzip -o /opt/deploy/i2b2core-src-1709b.zip -d /opt/deploy/

#unzip -o axis2.war.zip



###########################
# Fin des paramètre
#echo "UNZIPING i2b2core-src" $ROOTDIRECTORY/i2b2.zip ' to ' $ROOTDIRECTORY/
#unzip  -o $ROOTDIRECTORY/i2b2.zip -d $ROOTDIRECTORY/
i2b2_SOURCE=$ROOTDIRECTORY/$i2b2_SOURCE_DIR_NAME

echo 'repertoire i2b2 ==> ' $i2b2_source
#/$i2b2_SOURCE_DIR_NAME


###########################################################
#
# This part of the code is mostly from Florian Endel
# (https://github.com/FlorianEndel/i2b2-Docker/blob/master/4.1%20i2b2%20Server%20Common/Dockerfile)
#
# Sets up i2b2 app with parameters

###########################
#Server-commons
cd $i2b2_SOURCE/edu.harvard.i2b2.server-common/

sed -i "s#jboss.home=.*#jboss.home=$JBOSS_HOME_COMPILE#g" build.properties


$ANT_HOME/bin/ant clean dist deploy jboss_pre_deployment_setup


#######################
# PM  CELL
######################


cd $i2b2_SOURCE/edu.harvard.i2b2.pm
sed -i "s#jboss.home=.*#jboss.home=$JBOSS_HOME_COMPILE#g" build.properties

cd $i2b2_SOURCE/edu.harvard.i2b2.pm/etc/jboss
cp pm-ds.xml pm-ds.xml.orig

XML_SCHEMA="ds=http://www.jboss.org/ironjacamar/schema"



xmlstarlet ed -N $XML_SCHEMA  -u "//ds:connection-url" -v $CON_URL pm-ds.xml.orig | \
xmlstarlet ed -N $XML_SCHEMA  -u "//ds:driver-class" -v $DB_DRIVER_CLASS | \
xmlstarlet ed -N $XML_SCHEMA  -u "//ds:driver" -v $DB_DRIVER | \
xmlstarlet ed -N $XML_SCHEMA  -u "//ds:user-name" -v $i2b2_db_user_PM | \
xmlstarlet ed -N $XML_SCHEMA  -u "//ds:password" -v $i2b2_db_pass_PM \
> pm-ds.xml

cd $i2b2_SOURCE/edu.harvard.i2b2.pm

$ANT_HOME/bin/ant -f master_build.xml clean build-all deploy



cd ..

#######################
# ONT  CELL
######################

echo "ONT CELL"

# Configure Cells

cp /opt/ressources/ont-ds.xml $i2b2_SOURCE/edu.harvard.i2b2.ontology/etc/jboss/
appdirname=ontologyapp
cd $i2b2_SOURCE/edu.harvard.i2b2.ontology
sed -i "s#jboss.home=.*#jboss.home=$JBOSS_HOME_COMPILE/#g" build.properties


cd $i2b2_SOURCE/edu.harvard.i2b2.ontology/etc/spring/

sed -i "s#applicationdir=.*#applicationdir=$JBOSS_HOME_DOCKER/standalone/configuration/$appdirname#g" ontology_application_directory.properties

sed -i "s/ontology.bootstrapdb.metadataschema=.*/ontology.bootstrapdb.metadataschema=$i2b2_db_schema_HIVE/g" ontology.properties
sed -i "s#http://localhost:9090#http://localhost:$JBOSS_PORT#g" ontology.properties
sed -i "s/edu.harvard.i2b2.ontology.pm.serviceaccount.user=.*/edu.harvard.i2b2.ontology.pm.serviceaccount.user=$i2b2_AGGSERVICE_user/g" ontology.properties
sed -i "s/edu.harvard.i2b2.ontology.pm.serviceaccount.password=.*/edu.harvard.i2b2.ontology.pm.serviceaccount.password=$i2b2_AGGSERVICE_pass/g" ontology.properties
sed -i "s/Ontology.terminal.delimiter=.*/Ontology.terminal.delimiter=true/g" ontology.properties

cd ..


cd $i2b2_SOURCE/edu.harvard.i2b2.ontology/etc/jboss

cp ont-ds.xml ont-ds.xml.orig


XML_SCHEMA="ds=http://www.jboss.org/ironjacamar/schema"

xmlstarlet ed -N $XML_SCHEMA  -u "//ds:connection-url" -v $CON_URL ont-ds.xml.orig | \
xmlstarlet ed -N $XML_SCHEMA  -u "//ds:driver-class" -v $DB_DRIVER_CLASS | \
xmlstarlet ed -N $XML_SCHEMA  -u "//ds:driver" -v $DB_DRIVER | \
xmlstarlet ed -N $XML_SCHEMA  -u "(//ds:user-name)[1]" -v $i2b2_db_user_ONT | \
xmlstarlet ed -N $XML_SCHEMA  -u "(//ds:password)[1]" -v $i2b2_db_pass_ONT | \
xmlstarlet ed -N $XML_SCHEMA  -u "(//ds:user-name)[2]" -v  $i2b2_db_user_HIVE | \
xmlstarlet ed -N $XML_SCHEMA -u "(//ds:password)[2]" -v $i2b2_db_pass_HIVE | \
xmlstarlet ed -N $XML_SCHEMA  -u "(//ds:user-name)[3]" -v  $SHRINE_ONT_DB_USER  | \
xmlstarlet ed -N $XML_SCHEMA -u "(//ds:password)[3]" -v $SHRINE_ONT_DB_PASSWORD  \
> ont-ds.xml
#sed -i "s/SHRINE_ONT_USER/$SHRINE_ONT_USER/g" ont-ds.xml
#sed -i "s/SHRINE_ONT_PASSWORD/$SHRINE_ONT_PASSWORD/g" ont-ds.xml


cd $i2b2_SOURCE/edu.harvard.i2b2.ontology

sed -i "s#\${edu.harvard.i2b2.ontology.applicationdir}#\${jboss.home}/standalone/configuration/$appdirname#g" build.xml


$ANT_HOME/bin/ant -f master_build.xml clean build-all deploy




#######################
# CRC CELL
######################

echo "CRC CELL"


appdirname=crcapp
cd $i2b2_SOURCE/edu.harvard.i2b2.crc
sed -i "s#jboss.home=.*#jboss.home=$JBOSS_HOME_COMPILE/#g" build.properties


# Configure cells

cd $i2b2_SOURCE/edu.harvard.i2b2.crc/etc/spring/
sed -i "s#applicationdir=.*#applicationdir=$JBOSS_HOME_DOCKER/standalone/configuration/$appdirname#g" crc_application_directory.properties
sed -i "s#http://localhost:9090#http://localhost:$JBOSS_PORT#g" edu.harvard.i2b2.crc.loader.properties


cp CRCLoaderApplicationContext.xml CRCLoaderApplicationContext.xml.orig

xmlstarlet ed -u '//property[@name="driverClassName"]/@value' -v $DB_DRIVER_CLASS CRCLoaderApplicationContext.xml.orig | \
xmlstarlet ed -u '//property[@name="url"]/@value' -v $CON_URL | \
xmlstarlet ed -u '//property[@name="username"]/@value' -v $i2b2_db_user_HIVE | \
xmlstarlet ed -u '//property[@name="password"]/@value' -v $i2b2_db_pass_HIVE \
> CRCLoaderApplicationContext.xml \


sed -i "s/edu.harvard.i2b2.crc.loader.ds.lookup.servertype=.*/edu.harvard.i2b2.crc.loader.ds.lookup.servertype=$SERVER_TYPE/g" edu.harvard.i2b2.crc.loader.properties
sed -i "s#http://localhost:9090#http://localhost:$JBOSS_PORT#g" crc.properties
sed -i "s/queryprocessor.ds.lookup.servertype=.*/queryprocessor.ds.lookup.servertype=$SERVER_TYPE/g" crc.properties

cd $i2b2_SOURCE/edu.harvard.i2b2.crc/etc/jboss
cp crc-ds.xml crc-ds.xml.orig

XML_SCHEMA="ds=http://www.jboss.org/ironjacamar/schema"

xmlstarlet ed -N $XML_SCHEMA  -u "//ds:connection-url" -v $CON_URL crc-ds.xml.orig | \
xmlstarlet ed -N $XML_SCHEMA  -u "//ds:driver-class" -v $DB_DRIVER_CLASS | \
xmlstarlet ed -N $XML_SCHEMA  -u "//ds:driver" -v $DB_DRIVER | \
xmlstarlet ed -N $XML_SCHEMA  -u "(//ds:user-name)[1]" -v $i2b2_db_user_HIVE | \
xmlstarlet ed -N $XML_SCHEMA  -u "(//ds:password)[1]" -v $i2b2_db_pass_HIVE | \
xmlstarlet ed -N $XML_SCHEMA  -u "(//ds:user-name)[2]" -v $i2b2_db_user_CRC | \
xmlstarlet ed -N $XML_SCHEMA -u "(//ds:password)[2]" -v $i2b2_db_pass_CRC \
> crc-ds.xml



cd $i2b2_SOURCE/edu.harvard.i2b2.crc/

sed -i "s#\${edu.harvard.i2b2.crc.applicationdir}#\${jboss.home}/standalone/configuration/$appdirname#g" build.xml


$ANT_HOME/bin/ant -f master_build.xml clean build-all deploy




####################
# Cell Workplace WORK
###################


appdirname=workplaceapp
cd $i2b2_SOURCE/edu.harvard.i2b2.workplace
sed -i "s#jboss.home=.*#jboss.home=$JBOSS_HOME_COMPILE/#g" build.properties


# Configure Cells
cd $i2b2_SOURCE/edu.harvard.i2b2.workplace/etc/spring/
sed -i "s#applicationdir=.*#applicationdir=$JBOSS_HOME_DOCKER/standalone/configuration/$appdirname#g" workplace_application_directory.properties
sed -i "s#http://localhost:9090#http://localhost:$JBOSS_PORT#g" workplace.properties
sed -i "s/workplace.bootstrapdb.metadataschema=.*/workplace.bootstrapdb.metadataschema=$i2b2_db_schema_HIVE/g" workplace.properties

# Configure DB


cd $i2b2_SOURCE/edu.harvard.i2b2.workplace/etc/jboss

cp work-ds.xml work-ds.xml.orig

XML_SCHEMA="ds=http://www.jboss.org/ironjacamar/schema"

xmlstarlet ed -N $XML_SCHEMA  -u "//ds:connection-url" -v $CON_URL work-ds.xml.orig | \
xmlstarlet ed -N $XML_SCHEMA  -u "//ds:driver-class" -v $DB_DRIVER_CLASS | \
xmlstarlet ed -N $XML_SCHEMA  -u "//ds:driver" -v $DB_DRIVER | \
xmlstarlet ed -N $XML_SCHEMA  -u "(//ds:user-name)[1]" -v $i2b2_db_user_HIVE | \
xmlstarlet ed -N $XML_SCHEMA  -u "(//ds:password)[1]" -v $i2b2_db_pass_HIVE | \
xmlstarlet ed -N $XML_SCHEMA  -u "(//ds:user-name)[2]" -v $i2b2_db_user_WORK | \
xmlstarlet ed -N $XML_SCHEMA  -u "(//ds:password)[2]" -v $i2b2_db_pass_WORK \
> work-ds.xml
rm work-ds.xml.orig

# Deploy Cell
cd $i2b2_SOURCE/edu.harvard.i2b2.workplace/

sed -i "s#\${edu.harvard.i2b2.workplace.applicationdir}#\${jboss.home}/standalone/configuration/$appdirname#g" build.xml

$ANT_HOME/bin/ant -f master_build.xml clean build-all deploy



###########################
# Cell Filerepository FR
##########################
appdirname=frapp

cd $i2b2_SOURCE/edu.harvard.i2b2.fr

sed -i "s#jboss.home=.*#jboss.home=$JBOSS_HOME_COMPILE/#g" build.properties

# Configure Cells
cd $i2b2_SOURCE/edu.harvard.i2b2.fr/etc/spring/
sed -i "s#applicationdir=.*#applicationdir=$JBOSS_HOME_DOCKER/standalone/configuration/$appdirname#g" fr_application_directory.properties
sed -i "s#http://localhost:9090#http://localhost:$JBOSS_PORT#g" edu.harvard.i2b2.fr.properties

# Deploy Cell
cd $i2b2_SOURCE/edu.harvard.i2b2.fr

sed -i "s#\${edu.harvard.i2b2.fr.applicationdir}#\${jboss.home}/standalone/configuration/$appdirname#g" build.xml

$ANT_HOME/bin/ant -f master_build.xml clean build-all deploy


###########################
## Cell Identity Management IM

appdirname=imapp

cd $i2b2_SOURCE/edu.harvard.i2b2.im
sed -i "s#jboss.home=.*#jboss.home=$JBOSS_HOME_COMPILE#g" build.properties

# Configure Cells
cd $i2b2_SOURCE/edu.harvard.i2b2.im/etc/spring/
sed -i "s#applicationdir=.*#applicationdir=$JBOSS_HOME_DOCKER/standalone/configuration/$appdirname#g" im_application_directory.properties
sed -i "s#http://localhost:9090#http://localhost:$JBOSS_PORT#g" im.properties
sed -i "s/im.checkPatientInProject=.*/im.checkPatientInProject=true/g" im.properties

# Configure DB
cd $i2b2_SOURCE/edu.harvard.i2b2.im/etc/jboss
cp im-ds.xml im-ds.xml.orig

XML_SCHEMA="ds=http://www.jboss.org/ironjacamar/schema"

xmlstarlet ed -N $XML_SCHEMA  -u "//ds:connection-url" -v $CON_URL im-ds.xml.orig | \
xmlstarlet ed -N $XML_SCHEMA  -u "//ds:driver-class" -v $DB_DRIVER_CLASS | \
xmlstarlet ed -N $XML_SCHEMA  -u "//ds:driver" -v $DB_DRIVER | \
xmlstarlet ed -N $XML_SCHEMA  -u "(//ds:user-name)[1]" -v $i2b2_db_user_HIVE | \
xmlstarlet ed -N $XML_SCHEMA  -u "(//ds:password)[1]" -v $i2b2_db_pass_HIVE | \
xmlstarlet ed -N $XML_SCHEMA  -u "(//ds:user-name)[2]" -v $i2b2_db_user_IM | \
xmlstarlet ed -N $XML_SCHEMA  -u "(//ds:password)[2]" -v $i2b2_db_pass_IM \
> im-ds.xml
rm im-ds.xml.orig

# Deploy Cell
cd $i2b2_SOURCE/edu.harvard.i2b2.im

sed -i "s#\${edu.harvard.i2b2.im.applicationdir}#\${jboss.home}/standalone/configuration/$appdirname#g" build.xml

$ANT_HOME/bin/ant -f master_build.xml clean build-all deploy

#################################
#
# End of FLorian Endel's code
# (https://github.com/FlorianEndel/i2b2-Docker/blob/master/4.1%20i2b2%20Server%20Common/Dockerfile)
#
#

###################
#Install axis 2
mv $ROOTDIRECTORY/axis2.war $JBOSS_HOME_COMPILE/standalone/deployments/i2b2.war/
mv $JBOSS_HOME_COMPILE/standalone/deployments/i2b2.war/axis2.war $JBOSS_HOME_COMPILE/standalone/deployments/i2b2.war/axis2.zip
unzip -o $JBOSS_HOME_COMPILE/standalone/deployments/i2b2.war/axis2.zip -d $JBOSS_HOME_COMPILE/standalone/deployments/i2b2.war/
rm $JBOSS_HOME_COMPILE/standalone/deployments/i2b2.war/axis2.zip

##########################
# Build Docker
cd $ROOTDIRECTORY

mv /opt/deployments/standalone/configuration/* /opt/jboss/wildfly/standalone/configuration

cp /opt/deployments/standalone/deployments/i2b2.war/ /opt/jboss/wildfly/standalone/deployments/i2b2.war/ -R
touch /opt/jboss/wildfly/standalone/deployments/i2b2.war.dodeploy

cp /opt/deployments/standalone/deployments/pm-ds.xml /opt/jboss/wildfly/standalone/deployments/pm-ds.xml
touch /opt/jboss/wildfly/standalone/deployments/pm-ds.xml.dodeploy

cp /opt/deployments/standalone/deployments/crc-ds.xml /opt/jboss/wildfly/standalone/deployments/crc-ds.xml
touch /opt/jboss/wildfly/standalone/deployments/crc-ds.xml.dodeploy

cp /opt/deployments/standalone/deployments/ont-ds.xml /opt/jboss/wildfly/standalone/deployments/ont-ds.xml
touch /opt/jboss/wildfly/standalone/deployments/ont-ds.xml.dodeploy

cp /opt/deployments/standalone/deployments/work-ds.xml /opt/jboss/wildfly/standalone/deployments/work-ds.xml
touch /opt/jboss/wildfly/standalone/deployments/work-ds.xml.dodeploy

cp /opt/deployments/standalone/deployments/im-ds.xml /opt/jboss/wildfly/standalone/deployments/im-ds.xml
touch /opt/jboss/wildfly/standalone/deployments/im-ds.xml.dodeploy

#docker build  --tag=wildfly-app .
sed -i "s#false#true#g" /opt/deploy/deployed
