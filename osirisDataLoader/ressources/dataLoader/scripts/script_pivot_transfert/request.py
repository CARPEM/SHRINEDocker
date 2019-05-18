# -*- coding: utf-8 -*-
"""
Created 2018/01/05

@author: David BAUDOIN

fonction : script de creation de requetes SQL

"""

class SQL_request:
    # construction de l'objet
    def __init__(self):
        self.dic_data = {}

    def write_insert_i2b2_data(self, dic_data):
        request = ''
        if dic_data['table'] == 'patient_dimension':
            request = 'UPDATE i2b2demodata.patient_dimension SET ' + dic_data['var'] + ' = %s WHERE patient_num = %s;'
        elif dic_data['table'] == 'visit_dimension':
            request = 'UPDATE i2b2demodata.visit_dimension SET ' + dic_data['var'] + ' = %s WHERE patient_num = %s AND encounter_num = %s;'
        elif dic_data['table'] == 'concept_dimension':
            request = 'INSERT INTO i2b2demodata.observation_fact (patient_num, encounter_num, start_date, concept_cd, tval_char, nval_num, import_date, modifier_cd, instance_num, sourcesystem_cd, provider_id,end_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)'
        return request

    def write_insert_patient_dim(self):
        request = 'INSERT INTO i2b2demodata.patient_dimension (patient_num, sourcesystem_cd) VALUES (%s, %s);'
        return request

    def write_insert_patient_mapping(self):
        request = 'INSERT INTO i2b2demodata.patient_mapping (patient_num, patient_ide, patient_ide_source, project_id) VALUES (%s, %s, %s, %s);'
        return request

    def write_insert_visit_dim(self):
        request = 'INSERT INTO i2b2demodata.visit_dimension (patient_num, encounter_num, sourcesystem_cd) VALUES (%s, %s, %s);'
        return request

    def write_obsdata_csv_file(self, dic_data):
        raw=str(dic_data['patient_num']) + ';'
        raw += str(dic_data['encounter_num']) + ';'
        raw += str(dic_data['concept_cd']) + ';'
        raw += str(dic_data['provider_id']) + ';'
        raw += str(dic_data['modifier_cd']) + ';'
        raw += str(dic_data['instance_num']) + ';'
        raw += str(dic_data['date']) + ';'
        raw += str(dic_data['tvalue']) + ';'
        raw += str(dic_data['nvalue']) + ';'
        raw += str(dic_data['sourcesystem_cd'])
        raw += '\n'
        return raw
