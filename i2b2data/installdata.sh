#!/bin/bash

source $SECRETS

i2b2datahome=/opt/i2b2data

export host=$I2B2_DB_HOST

dbtype=$SERVER_TYPE
dbdriver=$DB_DRIVER_CLASS
dbproject=demo


!/bin/bash
 wait-for-postgres.sh

set -e

echo $POSTGRES_PASSWORD $host $POSTGRES_USER
until PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER"  -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"

sh /opt/initdb.sh

##############################

dbusername=$i2b2_db_user_CRC
dbpassword=$i2b2_db_pass_CRC
dburl="$CON_URL?searchpath=$dbusername"

cd $i2b2datahome/edu.harvard.i2b2.data/Release_1-7/NewInstall/Crcdata

echo $dburl

sed -i "s#db.type=.*#db.type=$dbtype#g" db.properties
sed -i "s#db.username=.*#db.username=$dbusername#g" db.properties
sed -i "s#db.password=.*#db.password=$dbpassword#g" db.properties
sed -i "s#db.driver=.*#db.driver=$dbdriver#g" db.properties
sed -i "s#db.url=.*#db.url=$dburl#g" db.properties
sed -i "s#db.project=.*#db.project=$dbproject#g" db.properties


/opt/ant/bin/ant -f data_build.xml create_crcdata_tables_release_1-7
/opt/ant/bin/ant -f data_build.xml create_procedures_release_1-7
/opt/ant/bin/ant -f data_build.xml db_demodata_load_data


##############################

dbusername=$i2b2_db_user_HIVE
dbpassword=$i2b2_db_pass_HIVE
dburl="$CON_URL?searchpath=$dbusername"


cd $i2b2datahome/edu.harvard.i2b2.data/Release_1-7/NewInstall/Hivedata


sed -i "s#db.type=.*#db.type=$dbtype#g" db.properties
sed -i "s#db.username=.*#db.username=$dbusername#g" db.properties
sed -i "s#db.password=.*#db.password=$dbpassword#g" db.properties
sed -i "s#db.driver=.*#db.driver=$dbdriver#g" db.properties
sed -i "s#db.url=.*#db.url=$dburl#g" db.properties
sed -i "s#db.project=.*#db.project=$dbproject#g" db.properties

sed -i "s#public#i2b2demodata#g" scripts/crc_db_lookup_postgresql_insert_data.sql
sed -i "s#public#i2b2imata#g" scripts/im_db_lookup_postgresql_insert_data.sql
sed -i "s#public#i2b2metadata#g" scripts/ont_db_lookup_postgresql_insert_data.sql
sed -i "s#public#i2b2workdata#g" scripts/work_db_lookup_postgresql_insert_data.sql



/opt/ant/bin/ant -f data_build.xml create_hivedata_tables_release_1-7
/opt/ant/bin/ant -f data_build.xml db_hivedata_load_data

##############################

dbusername=$i2b2_db_user_IM
dbpassword=$i2b2_db_pass_IM
dburl="$CON_URL?searchpath=$dbusername"

cd $i2b2datahome/edu.harvard.i2b2.data/Release_1-7/NewInstall/Imdata


sed -i "s#db.type=.*#db.type=$dbtype#g" db.properties
sed -i "s#db.username=.*#db.username=$dbusername#g" db.properties
sed -i "s#db.password=.*#db.password=$dbpassword#g" db.properties
sed -i "s#db.driver=.*#db.driver=$dbdriver#g" db.properties
sed -i "s#db.url=.*#db.url=$dburl#g" db.properties
sed -i "s#db.project=.*#db.project=$dbproject#g" db.properties


/opt/ant/bin/ant -f data_build.xml create_imdata_tables_release_1-7
/opt/ant/bin/ant -f data_build.xml db_imdata_load_data


##############################
dbusername=$i2b2_db_user_ONT
dbpassword=$i2b2_db_pass_ONT
dburl="$CON_URL?searchpath=$dbusername"

cd $i2b2datahome/edu.harvard.i2b2.data/Release_1-7/NewInstall/Metadata


sed -i "s#db.type=.*#db.type=$dbtype#g" db.properties
sed -i "s#db.username=.*#db.username=$dbusername#g" db.properties
sed -i "s#db.password=.*#db.password=$dbpassword#g" db.properties
sed -i "s#db.driver=.*#db.driver=$dbdriver#g" db.properties
sed -i "s#db.url=.*#db.url=$dburl#g" db.properties
sed -i "s#db.project=.*#db.project=$dbproject#g" db.properties


/opt/ant/bin/ant -f data_build.xml create_metadata_tables_release_1-7
/opt/ant/bin/ant -f data_build.xml db_metadata_load_data


##############################

dbusername=$i2b2_db_user_PM
dbpassword=$i2b2_db_pass_PM
dburl="$CON_URL?searchpath=$dbusername"


cd $i2b2datahome/edu.harvard.i2b2.data/Release_1-7/NewInstall/Pmdata


sed -i "s#db.type=.*#db.type=$dbtype#g" db.properties
sed -i "s#db.username=.*#db.username=$dbusername#g" db.properties
sed -i "s#db.password=.*#db.password=$dbpassword#g" db.properties
sed -i "s#db.driver=.*#db.driver=$dbdriver#g" db.properties
sed -i "s#db.url=.*#db.url=$dburl#g" db.properties
sed -i "s#db.project=.*#db.project=$dbproject#g" db.properties


/opt/ant/bin/ant -f data_build.xml create_pmdata_tables_release_1-7
/opt/ant/bin/ant -f data_build.xml db_pmdata_load_data

##############################

dbusername=$i2b2_db_user_WORK
dbpassword=$i2b2_db_pass_WORK
dburl="$CON_URL?searchpath=$dbusername"


cd $i2b2datahome/edu.harvard.i2b2.data/Release_1-7/NewInstall/Workdata


sed -i "s#db.type=.*#db.type=$dbtype#g" db.properties
sed -i "s#db.username=.*#db.username=$dbusername#g" db.properties
sed -i "s#db.password=.*#db.password=$dbpassword#g" db.properties
sed -i "s#db.driver=.*#db.driver=$dbdriver#g" db.properties
sed -i "s#db.url=.*#db.url=$dburl#g" db.properties
sed -i "s#db.project=.*#db.project=$dbproject#g" db.properties


/opt/ant/bin/ant -f data_build.xml create_workdata_tables_release_1-7
/opt/ant/bin/ant -f data_build.xml db_workdata_load_data

#################
# Update i2b2hive url for i2b2 default local cells
# namespace is jboss due to docker compose config

PGPASSWORD="$POSTGRES_PASSWORD" psql  -h "$host" -U "$POSTGRES_USER"  -c "UPDATE $i2b2_db_schema_PM.pm_cell_data set url='http://$CRC_HOST:$CRC_PORT/i2b2/services/QueryToolService/' where cell_id='CRC'"
PGPASSWORD="$POSTGRES_PASSWORD" psql  -h "$host" -U "$POSTGRES_USER"  -c "UPDATE $i2b2_db_schema_PM.pm_cell_data set url='http://$ONT_HOST:$ONT_PORT/i2b2/services/OntologyService/' where cell_id='ONT'"
PGPASSWORD="$POSTGRES_PASSWORD" psql  -h "$host" -U "$POSTGRES_USER"  -c "UPDATE $i2b2_db_schema_PM.pm_cell_data set url='http://$IM_HOST:$IM_PORT/i2b2/services/IMService/' where cell_id='IM'"
PGPASSWORD="$POSTGRES_PASSWORD" psql  -h "$host" -U "$POSTGRES_USER"	 -c "UPDATE $i2b2_db_schema_PM.pm_cell_data set url='http://$FR_HOST:$FR_PORT/i2b2/services/FRService/' where cell_id='FRC'"
PGPASSWORD="$POSTGRES_PASSWORD" psql  -h "$host" -U "$POSTGRES_USER"	 -c "UPDATE $i2b2_db_schema_PM.pm_cell_data set url='http://$WORK_HOST:$WORK_PORT/i2b2/services/WorkplaceService/' where cell_id='WORK'"
