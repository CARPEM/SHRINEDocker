# -*- coding: utf-8 -*-
"""
Created on 2018/10/09

@author: Vianney jouhet

fonction set shrine users (shrine to access crc and shrine users)
"""

from os import environ
from i2b2PMInteraction import i2b2_pm_interaction

def main():
    PM_HOST=environ['I2B2_HOST']
    PM_PORT=environ['I2B2_PORT']
    WEBCLIENT_HOST=environ['WEBCLIENT_HOST']
    WEBCLIENT_PORT=environ['WEBCLIENT_PORT']

    I2B2_DOMAIN=environ['I2B2_DOMAIN']

    SHRINE_USER=environ['SHRINE_USER']
    SHRINE_USER_PASSWORD=environ['SHRINE_USER_PASSWORD']

    SHRINE_CRC_USER=environ['SHRINE_CRC_USER']
    SHRINE_CRC_PASSWORD=environ['SHRINE_CRC_PASSWORD']

    # QEP_USER=environ['QEP_USER']
    QEP_PASSWORD=environ['QEP_PASSWORD']

    # STEWARD_USER=environ['STEWARD_USER']
    STEWARD_PASSWORD=environ['STEWARD_PASSWORD']

    I2B2_CRC_PROJECT_ID=environ['I2B2_CRC_PROJECT_ID']
    SHRINE_ONT_PROJECT_ID=environ['SHRINE_ONT_PROJECT_ID']

    I2B2_ADMIN=environ['I2B2_ADMIN']
    I2B2_ADMIN_PASSWORD=environ['I2B2_ADMIN_PASSWORD']
    #set pm connection
    pm=i2b2_pm_interaction(I2B2_ADMIN,I2B2_ADMIN_PASSWORD,I2B2_DOMAIN,PM_HOST,PM_PORT,WEBCLIENT_HOST,WEBCLIENT_PORT)

    ########### i2b2 crc shrine user ################
    #create i2b2 shrine user (obfucated)
    pm.adduser(SHRINE_CRC_USER,SHRINE_CRC_PASSWORD,'Shrine crc user','false','')
    pm.addrole(SHRINE_CRC_USER,"USER",I2B2_CRC_PROJECT_ID)
    # pm.addrole(SHRINE_CRC_USER,"DATA_OBFSC",I2B2_CRC_PROJECT_ID)
    # pm.addrole(SHRINE_CRC_USER,"DATA_DEID",I2B2_CRC_PROJECT_ID)
    # pm.addrole(SHRINE_CRC_USER,"DATA_AGG",I2B2_CRC_PROJECT_ID)
    # pm.addrole(SHRINE_CRC_USER,"DATA_LDS",I2B2_CRC_PROJECT_ID)
    pm.addrole(SHRINE_CRC_USER,"DATA_PROT",I2B2_CRC_PROJECT_ID)

    pm.adduser(SHRINE_USER,SHRINE_USER_PASSWORD,'SHRINE User','false','')
    pm.addrole(SHRINE_USER,"USER",SHRINE_ONT_PROJECT_ID)
    pm.addrole(SHRINE_USER,"DATA_OBFSC",SHRINE_ONT_PROJECT_ID)

    pm.adduser('qep',QEP_PASSWORD,'SHRINE QEP User','false','')
    # pm.addrole(QEP_USER,"USER",SHRINE_ONT_PROJECT_ID)
    # pm.addrole(QEP_USER,"DATA_OBFSC",SHRINE_ONT_PROJECT_ID)
    # pm.setuserparam(QEP_USER,'qep','T','true')

    pm.adduser('shrine_steward',STEWARD_PASSWORD,'SHRINE Data Steward User','false','')
    # pm.addrole(STEWARD_USER,"USER",SHRINE_ONT_PROJECT_ID)
    # pm.addrole(STEWARD_USER,"DATA_OBFSC",SHRINE_ONT_PROJECT_ID)
    # pm.setuserparam(STEWARD_USER,'DataSteward','T','true')


if __name__ == '__main__':
    main()
