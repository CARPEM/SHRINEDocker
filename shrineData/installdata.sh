#!/bin/bash

source $SECRETS

export host=$I2B2_DB_HOST

mysql -h "$SHRINE_DB_HOST" -u root -p$MYSQL_ROOT_PASSWORD < /opt/sql/init.sql
mysql -h "$SHRINE_DB_HOST" -u root -p$MYSQL_ROOT_PASSWORD -e "GRANT ALL privileges ON *.* TO "$MYSQL_USER"";

echo "Executing adapter.sql"
mysql -h "$SHRINE_DB_HOST" -u $MYSQL_USER -p$MYSQL_PASSWORD adapterAuditDB < /opt/sql/adapter.sql

echo "Executing qepAudit.sql"
mysql -h "$SHRINE_DB_HOST" -u $MYSQL_USER -p$MYSQL_PASSWORD qepAuditDB < /opt/sql/qepAudit.sql

echo "Executing shrine_query_history.sql"
mysql -h "$SHRINE_DB_HOST" -u $MYSQL_USER -p$MYSQL_PASSWORD shrine_query_history < /opt/sql/shrine_query_history.sql

echo "Executing hub.sql"
mysql -h "$SHRINE_DB_HOST" -u $MYSQL_USER -p$MYSQL_PASSWORD shrine_query_history < /opt/sql/hub.sql

echo "Executing steward.sql"
mysql -h "$SHRINE_DB_HOST" -u $MYSQL_USER -p$MYSQL_PASSWORD stewardDB < /opt/sql/steward.sql

echo "Executing adapter.sql"
mysql -h "$SHRINE_DB_HOST" -u root -p$MYSQL_ROOT_PASSWORD -e "GRANT ALL privileges ON *.* TO "$MYSQL_USER"";


PGPASSWORD="$i2b2_db_pass_PM" psql  	-d "$POSTGRES_DB"	-h "$I2B2_DB_HOST" -U "$i2b2_db_user_PM"  -f /opt/sql/qepuser.sql
# PGPASSWORD="$i2b2_db_pass_PM" psql  	-d "$POSTGRES_DB"	-h "$I2B2_DB_HOST" -U "$i2b2_db_user_PM"  -f /opt/sql/shrineuser.sql
PGPASSWORD="$i2b2_db_pass_PM" psql  	-d "$POSTGRES_DB"	-h "$I2B2_DB_HOST" -U "$i2b2_db_user_PM"  -f /opt/sql/stewarduser.sql
PGPASSWORD="$i2b2_db_pass_PM" psql  	-d "$POSTGRES_DB"	-h "$I2B2_DB_HOST" -U "$i2b2_db_user_PM"  -f /opt/sql/addCellsPm.sql
PGPASSWORD="$i2b2_db_pass_HIVE" psql  	-d "$POSTGRES_DB"	-h "$I2B2_DB_HOST" -U "$i2b2_db_user_HIVE"  -f /opt/sql/db_lookups.sql

# PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$I2B2_DB_HOST" -U "$POSTGRES_USER"  -f /opt/sql/createshrineont.sql

PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER"  -c "Create schema $SHRINE_ONT_DB_SCHEMA"
PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER"  -c "CREATE USER $SHRINE_ONT_DB_USER WITH PASSWORD '$SHRINE_ONT_DB_PASSWORD'"
PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER"  -c "GRANT ALL PRIVILEGES ON schema $SHRINE_ONT_DB_SCHEMA to $SHRINE_ONT_DB_USER"


PGPASSWORD="$SHRINE_ONT_DB_PASSWORD" psql  -h "$I2B2_DB_HOST" -d "$POSTGRES_DB" -U "$SHRINE_ONT_DB_USER"  -f /opt/sql/ontology_create_tables.sql
PGPASSWORD="$SHRINE_ONT_DB_PASSWORD" psql  -h "$I2B2_DB_HOST" -d "$POSTGRES_DB" -U "$SHRINE_ONT_DB_USER"  -f /opt/sql/demoontology.sql	> /dev/null
PGPASSWORD="$SHRINE_ONT_DB_PASSWORD" psql  -h "$I2B2_DB_HOST" -d "$POSTGRES_DB" -U "$SHRINE_ONT_DB_USER"  -f /opt/sql/schemes4shineont.sql

PGPASSWORD="$SHRINE_ONT_DB_PASSWORD" psql  -h "$I2B2_DB_HOST" -d "$POSTGRES_DB" -U "$SHRINE_ONT_DB_USER" -c "INSERT into shrine_ont.TABLE_ACCESS ( C_TABLE_CD, C_TABLE_NAME, C_PROTECTED_ACCESS, C_HLEVEL, C_NAME, C_FULLNAME, C_SYNONYM_CD, C_VISUALATTRIBUTES, C_TOOLTIP, C_FACTTABLECOLUMN, C_DIMTABLENAME, C_COLUMNNAME, C_COLUMNDATATYPE, C_DIMCODE, C_OPERATOR) values ( 'SHRINE', 'SHRINE', 'N', 0, 'SHRINE Ontology', '\SHRINE\', 'N', 'CA', 'SHRINE Ontology', 'concept_cd', 'concept_dimension', 'concept_path', 'T', '\SHRINE\', 'LIKE');"
