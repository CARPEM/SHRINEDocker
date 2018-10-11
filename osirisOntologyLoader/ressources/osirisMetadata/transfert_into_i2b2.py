# -*- coding: utf-8 -*-
"""
Created on 17/05/2018

@author: david
"""
import sys
import os
from SQLexecution import i2b2_interaction



def transfert (path_metafile, path_conceptfile, path_modiffile, path_shrine):

######################
# Modif Vianney on récupère les variable d'envirronement issues du dockerfile
# 03/10/2018
# @ V jouhet
######################

	# I2b2 db config
	DB_host = os.environ['I2B2_DB_HOST']
	DB_name = os.environ['POSTGRES_DB']
	DB_port = os.environ['I2B2_DB_PORT']
	BD_user = os.environ['i2b2_db_user_ONT']
	DB_password = os.environ['i2b2_db_pass_ONT']
	DB_type = os.environ['SERVER_TYPE']
	metadata_schema = os.environ['i2b2_db_schema_ONT']
	metadata_table = "osiris"
    # serveur galaxy
    # DB_host = 'egp-svldcarp3.egp.aphp.fr'
    # DB_name = 'i2b2'
    # DB_port = '49162'
    # BD_user = 'postgres'
    # DB_password = 'postgres'
    # DB_type = 'postgresql'

    # serveur local
    # DB_host = 'localhost'
    # DB_name = 'i2b2'
    # DB_port = '5432'
    # BD_user = 'postgres'
    # DB_password = 'postgres'
    # DB_type = 'postgresql'

    ### Ajout vianney on crée la table et on insert dans table access (i2b2)#####
	execution = i2b2_interaction(DB_type, DB_host, DB_name, DB_port, BD_user, DB_password)
	execution.create_metadata_table(metadata_table,metadata_schema)
	execution.insert_table_access(metadata_table,metadata_schema)
    ########################################

	execution.send_data(path_metafile, metadata_schema+'.'+metadata_table)
	execution.dbcon.commit()


	### Ajout vianney on crée la table et on insert dans table access (shrine)#####
	metadata_schema="shrine_ont"
	BD_user = os.environ['SHRINE_ONT_DB_USER']
	DB_password = os.environ['SHRINE_ONT_DB_PASSWORD']

	execution = i2b2_interaction(DB_type, DB_host, DB_name, DB_port, BD_user, DB_password)
	execution.create_metadata_table(metadata_table,metadata_schema)
	execution.insert_table_access(metadata_table,metadata_schema)
	execution.send_data_2(path_shrine, metadata_schema+'.'+metadata_table,("C_HLEVEL",
				  "C_FULLNAME",
				  "C_NAME",
				  "C_SYNONYM_CD",
				  "C_VISUALATTRIBUTES",
				  "C_TOTALNUM",
				  "C_BASECODE",
				  "C_METADATAXML",
				  "C_FACTTABLECOLUMN",
				  "C_TABLENAME",
				  "C_COLUMNNAME",
				  "C_COLUMNDATATYPE",
				  "C_OPERATOR",
				  "C_DIMCODE",
				  "C_COMMENT",
				  "C_TOOLTIP",
				  "UPDATE_DATE",
				  "DOWNLOAD_DATE",
				  "IMPORT_DATE",
				  "SOURCESYSTEM_CD",
				  "VALUETYPE_CD",
				  "M_APPLIED_PATH",
				  "M_EXCLUSION_CD"))
	execution.dbcon.commit()
    ########################################

	BD_user = os.environ['i2b2_db_user_CRC']
	DB_password = os.environ['i2b2_db_pass_CRC']
	execution = i2b2_interaction(DB_type, DB_host, DB_name, DB_port, BD_user, DB_password)
	execution.send_data(path_conceptfile, 'i2b2demodata.concept_dimension')
	execution.dbcon.commit()
	execution.send_data(path_modiffile, 'i2b2demodata.modifier_dimension')
	execution.dbcon.commit()

	execution.dbcon.commit()
	execution.dbcon.close()




def main():

	path_metafile = '/opt/see2i2b2_meta.txt'
	path_conceptfile = '/opt/see2i2b2_demo.txt'
	path_modiffile = '/opt/see2i2b2_modif.txt'
	path_shrine = '/opt/see2shrine_.txt'

	transfert (path_metafile, path_conceptfile, path_modiffile, path_shrine)




if __name__ == '__main__':
    main()
