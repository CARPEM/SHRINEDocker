FROM library/ubuntu:18.04

# ENV I2B2_DB_HOST=$I2B2_DB_HOST
# ENV SERVER_TYPE=$SERVER_TYPE
# ENV POSTGRES_DB=$POSTGRES_DB
# ENV POSTGRES_USER=$POSTGRES_USER
# ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD
#
# ENV i2b2_db_schema_CRC=$i2b2_db_schema_CRC
# ENV DB_DRIVER_CLASS=$DB_DRIVER_CLASS
# ENV CON_URL=$CON_URL
# ENV I2B2_CRC_PROJECT_ID=$I2B2_CRC_PROJECT_ID
#
# ENV PM_HOST=$PM_HOST
# ENV PM_PORT=$PM_PORT
# ENV ONT_HOST=$ONT_HOST
# ENV ONT_PORT=$ONT_PORT
# ENV CRC_HOST=$CRC_HOST
# ENV CRC_PORT=$CRC_PORT
# ENV FR_HOST=$FR_HOST
# ENV FR_PORT=$FR_PORT
# ENV WORK_HOST=$WORK_HOST
# ENV WORK_PORT=$WORK_PORT
#
#
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

RUN apt-get update \
&& apt-get install openjdk-8-jdk wget -y

ENV HTTPS_PROXY=false
ENV HTTP_PROXY=false

ADD ./wget_proxy_setup.sh /opt/wget_proxy_setup.sh
RUN chmod +x /opt/wget_proxy_setup.sh

RUN apt-get install unzip

RUN apt-get install postgresql -y

RUN wget https://www.i2b2.org/software/projects/installer/apache-ant-1.9.6-bin.zip \
	&& unzip apache-ant-1.9.6-bin.zip -d /opt \
	&& mv /opt/apache-ant-1.9.6/ /opt/ant/


RUN apt-get install xmlstarlet -y

ADD ./i2b2createdb-1710.zip /opt

RUN unzip /opt/i2b2createdb-1710.zip -d /opt \
	&& mv /opt/i2b2-data-master /opt/i2b2data/


ADD ./initdb.sh /opt
ADD ./installdata.sh /opt

RUN chmod +x /opt/initdb.sh
RUN chmod +x /opt/installdata.sh
ENTRYPOINT ["/opt/installdata.sh"]
