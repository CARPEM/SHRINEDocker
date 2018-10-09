FROM ubuntu

# ENV SHRINE_DB_HOST=$SHRINE_DB_HOST
# ENV MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD
# ENV MYSQL_USER=$MYSQL_USER
# ENV MYSQL_PASSWORD=$MYSQL_PASSWORD
#
# ENV I2B2_DB_HOST=$I2B2_DB_HOST
# ENV POSTGRES_DB=$POSTGRES_DB
# ENV POSTGRES_USER=$POSTGRES_USER
# ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD
#
# ENV PM_HOST=$PM_HOST
# ENV PM_PORT=$PM_PORT
#
# ENV i2b2_db_user_PM=$i2b2_db_user_PM
# ENV i2b2_db_pass_PM=$i2b2_db_pass_PM
# ENV i2b2_db_schema_PM=$i2b2_db_schema_PM
#
# ENV i2b2_db_user_HIVE=$i2b2_db_user_HIVE
# ENV i2b2_db_pass_HIVE=$i2b2_db_pass_HIVE
# ENV i2b2_db_schema_HIVE=$i2b2_db_schema_HIVE
#
# ENV SHRINE_ONT_PASSWORD=$SHRINE_ONT_PASSWORD
# ENV SHRINE_ONT_USER=$SHRINE_ONT_USER

RUN 	apt-get update \
	&& 	apt-get install mysql-client -y \
	&&	apt-get install postgresql -y

ADD ./installdata.sh /opt/installdata.sh
ADD ./init.sql /opt/sql/init.sql

#Add table creation sscript for mariadb
ADD ./adapter.sql /opt/sql/adapter.sql
ADD ./qepAudit.sql /opt/sql/qepAudit.sql
ADD ./shrine_query_history.sql /opt/sql/shrine_query_history.sql
ADD ./hub.sql /opt/sql/hub.sql
ADD ./steward.sql /opt/sql/steward.sql

#Add user insertion for i2b2 instance (posgresql)
ADD ./qepuser.sql /opt/sql/qepuser.sql
ADD ./shrineuser.sql /opt/sql/shrineuser.sql
ADD ./stewarduser.sql /opt/sql/stewarduser.sql

#Add shine_ont schema and data for shrine ontology
ADD ./createshrineont.sql /opt/sql/createshrineont.sql
ADD ./ontology_create_tables.sql /opt/sql/ontology_create_tables.sql
ADD ./schemes4shineont.sql /opt/sql/schemes4shineont.sql
ADD ./db_lookups.sql /opt/sql/db_lookups.sql

ADD ./demoontology.sql /opt/sql/demoontology.sql

#Registeer shrine cells to Pm
ADD ./addCellsPm.sql /opt/sql/addCellsPm.sql


RUN chmod +x /opt/installdata.sh
ENTRYPOINT ["/opt/installdata.sh"]
