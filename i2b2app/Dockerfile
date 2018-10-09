FROM jboss/wildfly:10.1.0.Final

USER root

#######################
# Nom des sources i2b2
# ENV i2b2_SOURCE_FILE_NAME=$i2b2_SOURCE_FILE_NAME
# #i2b2_SOURCE_FILE_NAME=$i2b2_SOURCE_FILE_NAME
#
# #######################
# # Nom du dossier après extraction
# #i2b2_SOURCE_DIR_NAME=$i2b2_SOURCE_DIR_NAME
# ENV i2b2_SOURCE_DIR_NAME=$i2b2_SOURCE_DIR_NAME
# ##########################
# # Paramètre de JBOSS
# ENV JBOSS_HOME_DOCKER=$JBOSS_HOME_DOCKER
# ENV JBOSS_PORT=$JBOSS_PORT
#
# #####################
# # Chemin de destination des fichier de complilation
# #JBOSS_HOME_COMPILE=$JBOSS_HOME_COMPILE
# ENV JBOSS_HOME_COMPILE=$JBOSS_HOME_COMPILE
# ##################
# # Chemin de ant sur le server
# ENV ANT_HOME=$ANT_HOME
#
# ###########################
# # Paramètre serveur de base de donnée
# #DB_DRIVER=$DB_DRIVER
# #SERVER_TYPE=$SERVER_TYPE
#
# ENV I2B2_DB_HOST=$I2B2_DB_HOST
# ENV POSTGRES_DB=$POSTGRES_DB
# ENV CON_URL=$CON_URL
# ENV DB_DRIVER_CLASS=$DB_DRIVER_CLASS
# ENV DB_DRIVER=$DB_DRIVER
# ENV SERVER_TYPE=$SERVER_TYPE
#
#
# ################################
# # Connexion aux schema
# ENV i2b2_db_user_HIVE=$i2b2_db_user_HIVE
# ENV i2b2_db_pass_HIVE=$i2b2_db_pass_HIVE
# ENV i2b2_db_schema_HIVE=$i2b2_db_schema_HIVE
#
# ENV i2b2_db_user_PM=$i2b2_db_user_PM
# ENV i2b2_db_pass_PM=$i2b2_db_pass_PM
# ENV i2b2_db_schema_PM=$i2b2_db_schema_PM
#
# ENV i2b2_AGGSERVICE_user=$i2b2_AGGSERVICE_user
# ENV i2b2_AGGSERVICE_pass=$i2b2_AGGSERVICE_pass
#
# ENV i2b2_db_user_CRC=$i2b2_db_user_CRC
# ENV i2b2_db_pass_CRC=$i2b2_db_pass_CRC
# ENV i2b2_db_schema_CRC=$i2b2_db_schema_CRC
#
# ENV i2b2_db_user_ONT=$i2b2_db_user_ONT
# ENV i2b2_db_pass_ONT=$i2b2_db_pass_ONT
# ENV i2b2_db_schema_ONT=$i2b2_db_schema_ONT
#
# ENV i2b2_db_user_WORK=$i2b2_db_user_WORK
# ENV i2b2_db_pass_WORK=$i2b2_db_pass_WORK
# ENV i2b2_db_schema_WORK=$i2b2_db_schema_WORK
#
# ENV i2b2_db_user_IM=$i2b2_db_user_IM
# ENV i2b2_db_pass_IM=$i2b2_db_pass_IM
# ENV i2b2_db_schema_IM=$i2b2_db_schema_IM
#
# ENV db_project=$db_project
#
#
# ###################""
# #
# #	SHRINE
# #
# ENV SHRINE_ONT_USER=$SHRINE_ONT_USER
# ENV SHRINE_ONT_PASSWORD=$SHRINE_ONT_PASSWORD


RUN mkdir /opt/deploy

ADD ./ressources/i2b2core-src-1709c.zip /opt/deploy/i2b2core-src-1709c.zip
RUN unzip -o /opt/deploy/i2b2core-src-1709c.zip -d /opt/deploy/
ADD ./ressources/ont-ds.xml.template /opt/ressources/ont-ds.xml


WORKDIR /opt/deploy/
RUN ls
ADD ./lib/postgresql-42.1.4.jar /opt/jboss/wildfly/standalone/deployments/postgresql-42.1.4.jar
ADD ./lib/xmlstarlet-1.6.1-1.el7.x86_64.rpm /opt/deploy/xmlstarlet.rpm
RUN rpm -ivh xmlstarlet.rpm

ADD ./lib/apache-ant-1.9.6-bin.zip /opt/deploy/ant.zip
RUN unzip ant.zip -d /opt \
        && mv /opt/apache-ant-1.9.6/ /opt/ant/

ADD ./lib/axis2-1.7.1-war.zip /opt/deploy/axis2-war.zip
RUN unzip -o /opt/deploy/axis2-war.zip

WORKDIR /opt/deploy/

RUN touch deployed
RUN echo 'false'>deployed
ADD ./ressources/parametrage.sh /opt/deploy/parametrage.sh
RUN chmod +x /opt/deploy/parametrage.sh
ADD ./ressources/start.sh /opt/deploy/start.sh
RUN chmod +x /opt/deploy/start.sh

# RUN /opt/deploy/parametrage.sh



CMD ["/opt/deploy/start.sh"]
