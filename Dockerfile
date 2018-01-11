FROM ubuntu:14.04

# Dockerfile take from sebmate/Docker-i2b2 and upgrade
# read your proxy
ENV http_proxy= \
https_proxy=

RUN apt-get update
RUN apt-get install -y -y dos2unix vim unzip aptitude wget curl libcurl3 php5-curl apache2 libaio1 libapache2-mod-php5 perl sed bc nano openssh-server
RUN apt-get install -y -y openjdk-7-jre openjdk-7-jdk openjdk-7-jre-headless
RUN apt-get install -y -y dialog
RUN apt-get install -y -y postgresql-client

ENV wizardVer i2b2wizard_2016-02-16

COPY $wizardVer.zip /root/
WORKDIR /root
RUN unzip $wizardVer.zip

COPY quick_install.zip /root/$wizardVer
RUN unzip /root/$wizardVer/quick_install.zip

COPY i2b2createdb-1707.zip /root/$wizardVer/packages
COPY i2b2core-src-1707.zip /root/$wizardVer/packages
COPY i2b2webclient-1707.zip /root/$wizardVer/packages

COPY axis2-1.6.2-war.zip /root/$wizardVer/packages
COPY apache-ant-1.8.2-bin.zip /root/$wizardVer/packages
COPY jbossfiles /root/$wizardVer/packages/jbossfiles 
RUN cat x* > /root/$wizardVer/packages/jbossfiles/jbosssplit* /root/$wizardVer/packages/jboss-as-7.1.1.Final.zip
COPY jboss-as-7.1.1.Final.zip /root/$wizardVer/packages

#COPY oracle-xe-universal_10.2.0.1-1.1_i386.deb /root/$wizardVer/packages
#COPY libaio_0.3.104-1_i386.deb /root/$wizardVer/packages

WORKDIR /root/$wizardVer

EXPOSE 80
EXPOSE :6443

RUN chmod +x wizard.sh
RUN find . -name "*.sh" -type f -exec dos2unix {} \;

#RUN ./wizard.sh --docker oracle

RUN apt-get install --force-yes -y subversion
RUN apt-get install mysql-client --force-yes -y

ENV http_proxy= \
https_proxy= 

CMD /bin/bash
