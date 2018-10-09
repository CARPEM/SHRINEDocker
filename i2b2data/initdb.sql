pslql PGPASSWORD="i2b2" psql -h "$host" -U "i2b2"  -c "Create schema i2b2demodata"

CREATE USER i2b2demodata WITH PASSWORD 'demouser';
GRANT ALL PRIVILEGES ON schema i2b2demodata to i2b2demodata;

Create schema i2b2hive;
CREATE USER i2b2hive WITH PASSWORD 'demouser';
GRANT ALL PRIVILEGES ON schema i2b2hive to i2b2hive;

Create schema i2b2imdata;
CREATE USER i2b2imdata WITH PASSWORD 'demouser';
GRANT ALL PRIVILEGES ON schema i2b2imdata to i2b2imdata;

Create schema i2b2metadata;
CREATE USER i2b2metadata WITH PASSWORD 'demouser';
GRANT ALL PRIVILEGES ON schema i2b2metadata to i2b2metadata;

Create schema i2b2pm;
CREATE USER i2b2pm WITH PASSWORD 'demouser';
GRANT ALL PRIVILEGES ON schema i2b2pm to i2b2pm;

Create schema i2b2workdata;
CREATE USER i2b2workdata WITH PASSWORD 'demouser';
GRANT ALL PRIVILEGES ON schema i2b2workdata to i2b2workdata;

COMMIT;
