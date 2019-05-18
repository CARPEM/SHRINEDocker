###########################################################
#           loader for osiris osirisMetadata
#   Author Vianney jouhet
#   03/10/2018
#   Loads ontology data into i2b2 and shrine
##########################################################


FROM python:latest


# ENV ONT_HOST=$ONT_HOST
# ENV ONT_PORT=$ONT_PORT
#
# ENV I2B2_DB_HOST=$I2B2_DB_HOST
# ENV I2B2_DB_PORT=$I2B2_DB_PORT
# ENV SERVER_TYPE=$SERVER_TYPE
# ENV POSTGRES_DB=$POSTGRES_DB
# ENV POSTGRES_USER=$POSTGRES_USER
# ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD
#
# ENV i2b2_db_user_ONT=$i2b2_db_user_ONT
# ENV i2b2_db_pass_ONT=$i2b2_db_pass_ONT
# ENV i2b2_db_schema_ONT=$i2b2_db_schema_ONT
#
# ENV i2b2_db_user_CRC=$i2b2_db_user_CRC
# ENV i2b2_db_pass_CRC=$i2b2_db_pass_CRC
# ENV i2b2_db_schema_CRC=$i2b2_db_schema_CRC
#
# ENV SHRINE_ONT_USER=$SHRINE_ONT_USER
# ENV SHRINE_ONT_PASSWORD=$SHRINE_ONT_PASSWORD

RUN pip install psycopg2 cx_oracle mysql
RUN apt-get update --fix-missing \
    && apt-get install postgresql -y

WORKDIR /opt
ADD ./ressources/ /opt/
ADD ./mapping_files/ /opt/mapping_files/

# ADD ./ressources/ontologyLoader/loadOntology.sh /opt/loadOntology.sh

RUN chmod +x /opt/ontologyLoader/loadOntology.sh
RUN chmod +x /opt/dataLoader/loadOsirisData.sh
RUN chmod +x /opt/dataLoader/adaptTables.sh

ENTRYPOINT ["/bin/bash"]
