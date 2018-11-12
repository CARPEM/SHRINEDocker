FROM debian:latest

USER root

ENV HTTPS_PROXY=false
ENV HTTP_PROXY=false

RUN mkdir -p /opt/java
WORKDIR /opt/java
RUN apt-get update  \
	&& apt-get install wget -y

ADD ./ressources/wget_proxy_setup.sh /opt/wget_proxy_setup.sh
RUN chmod +x /opt/wget_proxy_setup.sh

RUN /opt/wget_proxy_setup.sh

RUN wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=a" "http://download.oracle.com/otn-pub/java/jdk/8u192-b12/750e1c8617c5452694857ad95c3ee230/jdk-8u192-linux-x64.tar.gz" \
	&& tar xzf jdk-8u192-linux-x64.tar.gz

RUN chown -R root: jdk1.8.0_*

#-- for JAVA (in case you have another version of Java installed)
RUN 	update-alternatives --install /usr/bin/java java /opt/java/jdk1.8.0_192/bin/java 1\
#-- for JAR (in case you have another version of Java installed)
	&& 	update-alternatives --install /usr/bin/jar jar /opt/java/jdk1.8.0_192/bin/jar 1\
#-- for JAVAC (in case you have another version of Java installed)
	&& 	update-alternatives --install /usr/bin/javac javac /opt/java/jdk1.8.0_192/bin/javac 1 \
	&&	update-alternatives --config javac  \
	&& 	rm /opt/java/jdk-8u192*.tar.gz

#-- setting JAVA variables
RUN 	export JAVA_HOME=/opt/java/jdk1.8.0_172 \
	&& 	export JRE_HOME=/opt/java/jdk1.8.0_172/jre \
	&&	export PATH=$PATH:/opt/java/jdk1.8.0_172/bin:/opt/java/jdk1.8.0_172/jre/bin

# ENV KEYSTORE_ALIAS=$KEYSTORE_ALIAS
# ENV KEYSTORE_HUMAN=$KEYSTORE_HUMAN
# ENV KEYSTORE_CITY=$KEYSTORE_CITY
# ENV KEYSTORE_STATE=$KEYSTORE_STATE
# ENV KEYSTORE_COUNTRY=$KEYSTORE_COUNTRY
# ENV KEYSTORE_PASSWORD=$KEYSTORE_PASSWORD
# ENV KEYSTORE_FILE=$KEYSTORE_FILE
#
# ENV SHRINE_HOST=$SHRINE_HOST
# ENV SHRINE_PORT=$SHRINE_PORT
# ENV SHRINE_WEBCLIENT_HOST=SHRINE_WEBCLIENT_HOST
# ENV SHRINE_WEBCLIENT_PORT=SHRINE_WEBCLIENT_HOST
#
# ENV SHRINE_HUB_HOST=$SHRINE_HUB_HOST
# ENV SHRINE_HUB_PORT=$SHRINE_HUB_PORT
#
# ENV SHRINE_DB_HOST=$SHRINE_DB_HOST
# ENV SHRINE_DB_PORT=$SHRINE_DB_PORT
# ENV MYSQL_USER=$MYSQL_USER
# ENV MYSQL_PASSWORD=$MYSQL_PASSWORD
#
# ENV NODE_NAME=$NODE_NAME
#
# ENV PM_HOST=$PM_HOST
# ENV PM_PORT=$PM_PORT
# ENV ONT_HOST=$ONT_HOST
# ENV ONT_PORT=$ONT_PORT
# ENV CRC_HOST=$CRC_HOST
# ENV CRC_PORT=$CRC_PORT
#
# ENV I2B2_DOMAIN=$I2B2_DOMAIN
# ENV I2B2_USER=$I2B2_USER
# ENV I2B2_PASSWORD=$I2B2_PASSWORD
# ENV I2B2_CRC_PROJECT_ID=$I2B2_CRC_PROJECT_ID
# ENV SHRINE_ONT_PROJECT_ID=$SHRINE_ONT_PROJECT_ID
#
 	ENV QEP_USER=qep
# ENV QEP_PASSWORD=$QEP_PASSWORD
#
# ENV IS_HUB=$IS_HUB

RUN	apt-get install -y postfix -y\
	&& 	apt-get install -y ntp -y \
	&& 	apt-get install unzip -y \
	&&	apt-get install vim -y

RUN apt-get install systemd -y


RUN mkdir -p /opt/shrine/tomcat

RUN 	wget https://archive.apache.org/dist/tomcat/tomcat-8/v8.5.28/bin/apache-tomcat-8.5.28.tar.gz \
	&&	tar xvf apache-tomcat-8.5.28.tar.gz -C /opt/shrine/tomcat --strip-components=1



WORKDIR /opt/shrine/tomcat

## Setting correct permissions for the Tomcat folders
RUN 	useradd -ms /bin/bash shrine \
	&&	chgrp -R shrine /opt/shrine/tomcat  \
	&&	chmod -R g+r conf \
	&&	chmod g+x conf \
	&&	chown -R shrine webapps/ work/ temp/ logs/

RUN mkdir -p /opt/java
WORKDIR /opt/java




ADD ./ressources/shrine-war-1.22.8.war /opt/shrine/tomcat/webapps/shrine.war
ADD ./ressources/steward-1.22.8.war /opt/shrine/tomcat/webapps/steward.war
ADD ./ressources/shrine-proxy-1.22.8.war /opt/shrine/tomcat/webapps/shrine-proxy.war
ADD ./ressources/dashboard-war-1.22.8.war /opt/shrine/tomcat/webapps/shrine-dashboard.war
ADD ./ressources/meta-war-1.22.8.war /opt/shrine/tomcat/webapps/shrine-metadata.war.war
ADD ./ressources/shrine-webclient-1.22.8-dist.zip /opt/shrine/tomcat/webapps/shrine-webclient-1.22.8-dist.zip

WORKDIR /opt/shrine/tomcat/webapps/
RUN unzip shrine-webclient-1.22.8-dist.zip

ADD ./tomcat/conf/context.xml.template /opt/shrine/tomcat/conf/context.xml.orig
ADD ./tomcat/conf/server.xml.template /opt/shrine/tomcat/conf/server.xml.orig
ADD ./tomcat/lib/shrine.conf.template /opt/shrine/tomcat/lib/shrine.conf.orig
ADD ./tomcat/shrine-webclient/i2b2_config_data.js.template 	/opt/shrine/tomcat/webapps/shrine-webclient/i2b2_config_data.js.orig
ADD ./tomcat/shrine-webclient/js-i2b2/cells/SHRINE/cell_config_data.js.template /opt/shrine/tomcat/webapps/shrine-webclient/js-i2b2/cells/SHRINE/cell_config_data.js.orig

ADD ./tomcat/build_shrine.sh /opt/shrine/tomcat/build_shrine.sh
RUN chmod +x /opt/shrine/tomcat/build_shrine.sh
WORKDIR /opt/shrine/tomcat
# RUN ./build_shrine.sh

ADD ./tomcat/lib/AdapterMappings.csv /opt/shrine/tomcat/lib/AdapterMappings.csv

RUN echo $KEYSTORE_ALIAS

WORKDIR /opt/shrine

RUN ln -s /opt/java/jdk1.8.0_192/bin/keytool /usr/local/bin/keytool

ADD ./ressources/start.sh /opt/shrine/start.sh
RUN chmod +x /opt/shrine/start.sh
ADD ./ressources/import-cert.sh /opt/shrine/import-cert.sh
RUN chmod +x /opt/shrine/import-cert.sh
ADD ./ressources/sign-cert.sh /opt/shrine/sign-cert.sh
RUN chmod +x /opt/shrine/sign-cert.sh
ADD ./ressources/initHubCa.sh /opt/shrine/initHubCa.sh
RUN chmod +x /opt/shrine/initHubCa.sh
ADD ./ressources/backup-cert.sh /opt/shrine/backup-cert.sh
RUN chmod +x /opt/shrine/backup-cert.sh
ADD ./ressources/restore-cert.sh /opt/shrine/restore-cert.sh
RUN chmod +x /opt/shrine/restore-cert.sh
RUN touch deployed
RUN echo 'false'>deployed

ENTRYPOINT ["/opt/shrine/start.sh"]
