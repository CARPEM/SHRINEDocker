# -*- coding: utf-8 -*-
"""
Created on 2018/10/08

@author: Vianney jouhet

fonction set i2b2 users (admin and user)
"""

from os import environ
from i2b2PMInteraction import i2b2_pm_interaction

def main():
    PM_HOST=environ['I2B2_HOST']
    PM_PORT=environ['I2B2_PORT']
    WEBCLIENT_HOST=environ['WEBCLIENT_HOST']
    WEBCLIENT_PORT=environ['WEBCLIENT_PORT']

    I2B2_DOMAIN=environ['I2B2_DOMAIN']
    I2B2_USER=environ['I2B2_USER']
    I2B2_PASSWORD=environ['I2B2_PASSWORD']
    I2B2_ADMIN=environ['I2B2_ADMIN']
    I2B2_ADMIN_PASSWORD=environ['I2B2_ADMIN_PASSWORD']

    I2B2_CRC_PROJECT_ID=environ['I2B2_CRC_PROJECT_ID']
    #set pm connection
    pm=i2b2_pm_interaction('i2b2','demouser',I2B2_DOMAIN,PM_HOST,PM_PORT,WEBCLIENT_HOST,WEBCLIENT_PORT)

    ########### i2b2 simple user ################
    #create i2b2 simple user (obfucated)

    pm.adduser(I2B2_USER,I2B2_PASSWORD,'Simple user','false','')
    pm.addrole(I2B2_USER,"USER",I2B2_CRC_PROJECT_ID)
    pm.addrole(I2B2_USER,"DATA_PROT",I2B2_CRC_PROJECT_ID)

    # delete demouser (default for i2b2)
    if I2B2_USER!='demo':
        pm.deleteuserrole('demo','USER',I2B2_CRC_PROJECT_ID)
        pm.deleteuserrole('demo','DATA_OBFSC',I2B2_CRC_PROJECT_ID)
        pm.deleteuserrole('demo','EDITOR',I2B2_CRC_PROJECT_ID)
        pm.deleteuser('demo')


    ########### i2b2 admin user ################""
    #create admin user

    #
    if I2B2_ADMIN!='i2b2':
        pm.adduser(I2B2_ADMIN,I2B2_ADMIN_PASSWORD,'Admin user','true','')
        pm.setadmin(I2B2_ADMIN)
        #set as admin
        pm.addrole(I2B2_ADMIN,"ADMIN",I2B2_CRC_PROJECT_ID)
        pm.addrole(I2B2_ADMIN,"DATA_OBFSC",I2B2_CRC_PROJECT_ID)
        #delete i2b2 (default admin user)
        pm=i2b2_pm_interaction(I2B2_ADMIN,I2B2_ADMIN_PASSWORD,I2B2_DOMAIN,PM_HOST,PM_PORT,WEBCLIENT_HOST,WEBCLIENT_PORT)
        pm.deleteuserrole('i2b2','DATA_OBFSC',I2B2_CRC_PROJECT_ID)
        pm.deleteuserrole('i2b2','USER',I2B2_CRC_PROJECT_ID)
        # pm.deleteuserrole('i2b2','USER',I2B2_CRC_PROJECT_ID)
        # pm.deleteuserrole('i2b2','MANAGER',I2B2_CRC_PROJECT_ID)
        # pm.deleteuserrole('i2b2','EDITOR',I2B2_CRC_PROJECT_ID)
        pm.deleteuser('i2b2')
    else:
        pm.setpassword(I2B2_ADMIN_PASSWORD)
        pm=i2b2_pm_interaction(I2B2_ADMIN,I2B2_ADMIN_PASSWORD,I2B2_DOMAIN,PM_HOST,PM_PORT,WEBCLIENT_HOST,WEBCLIENT_PORT)
        pm.addrole(I2B2_ADMIN,"ADMIN",I2B2_CRC_PROJECT_ID)
        pm.setadmin(I2B2_ADMIN)

if __name__ == '__main__':
    main()
