#!/bin/bash
source $SECRETS

echo "Adapt tables for OSIRIS (patient and visit)"
PGPASSWORD="$i2b2_db_pass_CRC" psql  	-d "$POSTGRES_DB"	-h "$I2B2_DB_HOST" -U "$i2b2_db_user_CRC"  -f /opt/dataLoader/scripts/adaptTables.sql
