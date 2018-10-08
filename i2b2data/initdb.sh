PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER"  -c "Create schema $i2b2_db_schema_CRC"

PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER"  -c "CREATE USER $i2b2_db_user_CRC WITH PASSWORD '$i2b2_db_pass_CRC'"
PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER"  -c "GRANT ALL PRIVILEGES ON schema $i2b2_db_schema_CRC to $i2b2_db_user_CRC"

PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER"  -c "Create schema $i2b2_db_schema_HIVE"
PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER"  -c "CREATE USER $i2b2_db_user_HIVE WITH PASSWORD '$i2b2_db_pass_HIVE'"
PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER"  -c "GRANT ALL PRIVILEGES ON schema $i2b2_db_schema_HIVE to $i2b2_db_user_HIVE"

PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER"  -c "Create schema $i2b2_db_schema_IM"
PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER"  -c "CREATE USER $i2b2_db_user_IM WITH PASSWORD '$i2b2_db_pass_IM'"
PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "i2b2"  -c "GRANT ALL PRIVILEGES ON schema $i2b2_db_schema_IM to $i2b2_db_user_IM"

PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER"  -c "Create schema $i2b2_db_schema_ONT"
PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER"  -c "CREATE USER $i2b2_db_user_ONT WITH PASSWORD '$i2b2_db_pass_ONT'"
PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER"  -c "GRANT ALL PRIVILEGES ON schema $i2b2_db_schema_ONT to $i2b2_db_user_ONT"

PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER"  -c "Create schema $i2b2_db_schema_PM"
PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER"  -c "CREATE USER $i2b2_db_user_PM WITH PASSWORD '$i2b2_db_pass_PM'"
PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER"  -c "GRANT ALL PRIVILEGES ON schema $i2b2_db_schema_PM to $i2b2_db_user_PM"

PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER"  -c "Create schema $i2b2_db_schema_WORK"
PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER"  -c "CREATE USER $i2b2_db_schema_WORK WITH PASSWORD '$i2b2_db_pass_WORK'"
PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER"  -c "GRANT ALL PRIVILEGES ON schema $i2b2_db_schema_WORK to $i2b2_db_user_WORK"

