###########################################################
#           Manage i2b2 user (interaction with PM_CELL)
#   Author Vianney jouhet
#   08/10/2018
#
##########################################################


FROM python:latest

RUN pip install requests

ADD ./resources/ /opt/resources

RUN chmod +x /opt/resources/setI2b2Users.sh
RUN chmod +x /opt/resources/setShrineUsers.sh

WORKDIR /opt/resources

ENTRYPOINT ["/bin/bash"]
