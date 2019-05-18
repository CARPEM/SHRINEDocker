# -*- coding: utf-8 -*-
"""
Created 2018/01/05

@author: David BAUDOIN

fonction : script d'interaction avec la base de donnees i2b2

"""

import psycopg2
import cx_Oracle as cx


class i2b2_interaction:

    # construction de l'objet
	def __init__(self, type_connection, DB_host, DB_name, DB_port, BD_user, DB_password):
		self.type_connection = type_connection
		self.DB_host = DB_host
		self.DB_name = DB_name
		self.DB_port = DB_port
		self.BD_user = BD_user
		self.DB_password = DB_password
		self.dbcon = ''

	def connect_i2b2 (self) :
		if self.type_connection.lower() == 'postgresql':
			config = 'host=' + self.DB_host + ' port=' + self.DB_port + ' dbname=' + self.DB_name + ' user=' + self.BD_user + ' password=' + self.DB_password
			self.dbcon = psycopg2.connect(config)
			cur = self.dbcon.cursor()
			return cur

		elif self.type_connection.lower() == 'oracle':
			dsn = cx.makedsn(self.DB_host, self.DB_port, sid='CDWEGP')
			self.dbcon = cx.connect(self.BD_user, self.DB_password, dsn)
			cur = self.dbcon.cursor()
			return cur

		return None

    ###### Ajout vianney méthode pour créer la table ################"
	def create_metadata_table(self,table,schema) :
		create_script = "CREATE TABLE "+ schema+"."+table.upper()
		create_script += "(	C_HLEVEL INT			NOT NULL, "
		create_script += "C_FULLNAME VARCHAR(700)	NOT NULL, "
		create_script += "C_NAME VARCHAR(2000)		NOT NULL, "
		create_script += "C_SYNONYM_CD CHAR(1)		NOT NULL, "
		create_script += "C_VISUALATTRIBUTES CHAR(3)	NOT NULL, "
		create_script += "C_TOTALNUM INT			NULL, "
		create_script += "C_BASECODE VARCHAR(200)	NULL, "
		create_script += "C_METADATAXML TEXT		NULL, "
		create_script += "C_FACTTABLECOLUMN VARCHAR(50)	NOT NULL, "
		create_script += "C_TABLENAME VARCHAR(50)	NOT NULL, "
		create_script += "C_COLUMNNAME VARCHAR(50)	NOT NULL, "
		create_script += "C_COLUMNDATATYPE VARCHAR(50)	NOT NULL, "
		create_script += "C_OPERATOR VARCHAR(10)	NOT NULL, "
		create_script += "C_DIMCODE VARCHAR(700)	NOT NULL, "
		create_script += "C_COMMENT TEXT			NULL, "
		create_script += "C_TOOLTIP VARCHAR(900)	NULL,"
		create_script += "M_APPLIED_PATH VARCHAR(700)	NOT NULL, "
		create_script += "UPDATE_DATE timestamp		NOT NULL, "
		create_script += "DOWNLOAD_DATE timestamp	NULL, "
		create_script += "IMPORT_DATE timestamp	NULL, "
		create_script += "SOURCESYSTEM_CD VARCHAR(50)	NULL, "
		create_script += "VALUETYPE_CD VARCHAR(50)	NULL,"
		create_script += "M_EXCLUSION_CD	VARCHAR(25) NULL,"
		create_script += "C_PATH	VARCHAR(700)   NULL,"
		create_script += "C_SYMBOL	VARCHAR(50)	NULL"
		create_script += ") ;"

		create_fullname_index = "CREATE INDEX META_FULLNAME_IDX_"+table+" ON "+schema+"."+table+"(C_FULLNAME)"
		create_applied_index = "CREATE INDEX META_APPLIED_PATH_IDX_"+table+" ON "+schema+"."+table+"(M_APPLIED_PATH)"
		create_exclusion_index = "CREATE INDEX META_EXCLUSION_IDX_"+table+" ON "+schema+"."+table+"(M_EXCLUSION_CD)"
		create_hlevel_index	= "CREATE INDEX META_HLEVEL_IDX_"+table+" ON "+schema+"."+table+"(C_HLEVEL)"
		create_synonym_index = "CREATE INDEX META_SYNONYM_IDX_"+table+" ON "+schema+"."+table+"(C_SYNONYM_CD)"

		cur = self.connect_i2b2()
		cur.execute("DROP TABLE IF EXISTS " + schema +"."+table.upper())
		cur.execute(create_script)
		cur.execute(create_fullname_index)
		cur.execute(create_applied_index)
		cur.execute(create_exclusion_index)
		cur.execute(create_hlevel_index)
		cur.execute(create_synonym_index)
		self.dbcon.commit()

	###### Ajout du chemin dans table_access ################"
	def insert_table_access(self,table,schema) :
		delete_table_access="DELETE FROM "+schema+".table_access where c_fullname='\\i2b2\\OSIRIS\\\'"
		insert_table_access="INSERT INTO " + schema + ".table_access  VALUES(\'"+table.upper()+"\',\'"+table.upper()+"\',\'N\',1,\'\\i2b2\\OSIRIS\\\',\'OSIRIS-Ontology\',\'N\',\'FA\',null,null,null,\'concept_cd\',\'concept_dimension\',\'concept_path\',\'T\',\'LIKE\',\'\\i2b2\\OSIRIS\\\',null,\'Ontology OSIRIS\',null,null,null,null)"
		cur = self.connect_i2b2()
		cur.execute(delete_table_access)
		self.dbcon.commit()
		cur.execute(insert_table_access)
		self.dbcon.commit()



	def send_data (self, input_file, table) :
		f = open (input_file, 'r')
		cursor = self.connect_i2b2()
		#cursor.execute(request_i2b2.encode('utf-8'))
		cursor.copy_from(f, table, sep=';', null='None')
		f.close()

	def send_data_2 (self, input_file, table,columns_def) :
		f = open (input_file, 'r')
		cursor = self.connect_i2b2()
		#cursor.execute(request_i2b2.encode('utf-8'))
		cursor.copy_from(f, table, sep=';', null='None',
			columns=columns_def)
		f.close()

	def truncate_data (self,schema,table) :
		truncate_data_sql="TRUNCATE TABLE " +schema+ "." + table
		cur = self.connect_i2b2()
		cur.execute(truncate_data_sql)
		self.dbcon.commit()

	def create_concept_dimension_file (self) :
		concept_dimension = open ('/opt/data_to_load/concept_dimension.txt', 'w')
		insert_data_sql="""
			SELECT distinct c_fullname,C_BASECODE,C_NAME,' ' as concept_blob,update_date,download_date,import_date,sourcesystem_cd,'1' as t
			FROM i2b2metadata.osiris
			WHERE C_VISUALATTRIBUTES like 'L%' or (C_VISUALATTRIBUTES like 'F%' AND C_BASECODE not like 'ID\_%') 
		"""
		cursor = self.connect_i2b2()
		cursor.execute(insert_data_sql)

		for row in cursor:
			for i in range(0,9):
				t=str(row[i]).replace("\\","\\\\")
				if i == 8 :
					concept_dimension.write(t+ "\n")
				else:
					concept_dimension.write(t + ";")

		concept_dimension.close()

	def create_modifier_dimension_file (self) :
		concept_dimension = open ('/opt/data_to_load/modifier_dimension.txt', 'w')
		insert_data_sql="""
			SELECT distinct c_fullname,C_BASECODE,C_NAME,' ' as concept_blob,update_date,download_date,import_date,sourcesystem_cd,'1' as t
			FROM i2b2metadata.osiris
			WHERE C_VISUALATTRIBUTES like 'R%'
		"""
		cursor = self.connect_i2b2()
		cursor.execute(insert_data_sql)

		for row in cursor:
			for i in range(0,9):
				t=str(row[i]).replace("\\","\\\\")
				if i == 8 :
					concept_dimension.write(t+ "\n")
				else:
					concept_dimension.write(t + ";")

		concept_dimension.close()
