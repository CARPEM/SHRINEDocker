# -*- coding: utf-8 -*-
"""
Created 2018/05/28

@author: david

"""
from script_pivot_transfert.SQLexecution import i2b2_interaction
from script_pivot_transfert.request import SQL_request

class PivotData:
    # construction de l'objet
    def __init__(self, link_patient, link_visit, link_modifier, dic_ref_files, file_PI, sourcedata):
        self.sourcedata = sourcedata
        self.file_PI = file_PI
        self.patient_val = self.read_auto_val_patient()
        self.dic_patient = {}
        self.dicData = {}
        self.link_patient = link_patient
        self.link_visit = link_visit
        self.link_modifier = link_modifier
        self.dic_ref_files = {}
        self.list_key_ref = self.create_dic_ref(dic_ref_files)
        self.error_message = ''

    def create_dic_ref(self, dic_ref_files):
        key_ref = {};i=0
        self.dic_ref_files = dic_ref_files
        for ref_var in dic_ref_files['ref_var']:
            key_ref[ref_var] = {}
            key_ref[ref_var]['var'] = []
            key_ref[ref_var]['name'] = dic_ref_files['ref_var'][i]
            key_ref[ref_var]['nameFile'] = dic_ref_files['filename'][i]
            key_ref[ref_var]['parentFileRef'] = dic_ref_files['parent_ref'][i]
            key_ref[ref_var]['listPatient'] = {}
            i += 1
        return key_ref

    def add_var_to_dic_ref (self, ref_var, var):
        self.list_key_ref[ref_var]['var'].append(var)

    def add_patient_dimension(self, dic_patient, dic_db_param):
        i = 0

        req_i2b2 = SQL_request()
        interac_i2b2 = i2b2_interaction(dic_db_param['DB_type'], dic_db_param['DB_host'], dic_db_param['DB_name'],
                                        dic_db_param['DB_port'], dic_db_param['BD_user'], dic_db_param['DB_password'])

        for id_patient in dic_patient[self.link_patient]:
            self.dicData[id_patient] = {}
            self.list_key_ref['Patient_Id']['listPatient'][id_patient] = self.dicData[id_patient]

            # create patient in i2b2 (i2b2demodata.patient_dimension, i2b2demodata.patient_mapping) !!!!!!!!!!!!!!!!!!!!
            interac_i2b2.insert_data(req_i2b2.write_insert_patient_mapping(), (self.patient_val, id_patient, self.sourcedata, 'OSIRIS'))
            interac_i2b2.insert_data(req_i2b2.write_insert_patient_dim(), [self.patient_val, 'TEST_OSIRIS'])
            self.patient_val += 1
            self.dic_patient[id_patient] = self.patient_val

            for var_data in dic_patient:
                if dic_patient[var_data][i] != '':
                    self.dicData[id_patient][var_data] = dic_patient[var_data][i]
            i += 1

        self.update_val_patient()

        for key in dic_patient :
            self.add_var_to_dic_ref('Patient_Id', key)

    def add_visit_dimension(self, dic_visit, dic_db_param):
        i = 0

        req_i2b2 = SQL_request()
        interac_i2b2 = i2b2_interaction(dic_db_param['DB_type'], dic_db_param['DB_host'], dic_db_param['DB_name'],
                                        dic_db_param['DB_port'], dic_db_param['BD_user'], dic_db_param['DB_password'])

        for id_patient in dic_visit[self.link_patient]:
            if self.link_visit not in self.dicData[id_patient].keys(): self.dicData[id_patient][self.link_visit] = {}
            self.dicData[id_patient][self.link_visit][dic_visit[self.link_modifier][i]] = {}
            if not id_patient in self.list_key_ref[self.link_visit]['listPatient'].keys():
                self.list_key_ref[self.link_visit]['listPatient'][id_patient] = {}
            self.list_key_ref[self.link_visit]['listPatient'][id_patient][dic_visit[self.link_modifier][i]]= self.dicData[id_patient][self.link_visit][dic_visit[self.link_modifier][i]]

            # create visit !!!
            interac_i2b2.insert_data(req_i2b2.write_insert_visit_dim(), [self.dic_patient[id_patient], dic_visit[self.link_modifier][i], self.sourcedata])


            for var_data in dic_visit:
                if var_data not in (self.link_patient, self.link_modifier):
                    if dic_visit[var_data][i] != '':
                        self.dicData[id_patient][self.link_visit][dic_visit[self.link_modifier][i]][var_data] = dic_visit[var_data][i]
            i += 1

        for key in dic_visit:
            self.add_var_to_dic_ref(self.link_visit, key)

    def add_file_into_data(self, dic_file, name_file):
        iaf = 0
        var_ref = self.search_ref(dic_file, name_file)
        for varfile in dic_file:
            self.add_var_to_dic_ref(var_ref, varfile)
        for patient in dic_file[self.link_patient]:
            idp = dic_file[self.link_modifier][iaf]
            ref = dic_file[self.list_key_ref[var_ref]['parentFileRef']][iaf]
            dicSubData = self.find_link_into_dicdata(patient, var_ref, idp, ref)
            for var_data in dic_file:
                if dic_file[var_data][iaf] != '':
                    dicSubData[var_data] = dic_file[var_data][iaf]
            iaf+=1

        for key in dic_file:
            self.add_var_to_dic_ref(var_ref, key)

    def find_link_into_dicdata(self, patient, var_ref, idp, ref):
        if not patient in self.list_key_ref[var_ref]['listPatient']:
            self.list_key_ref[var_ref]['listPatient'][patient] = {}
            self.add_key_ref(var_ref, patient, idp, ref)
        if not idp in self.list_key_ref[var_ref]['listPatient'][patient]:
            self.add_key_ref(var_ref, patient, idp, ref)
        #print (self.list_key_ref[var_ref]['listPatient'][patient][idp])
        return self.list_key_ref[var_ref]['listPatient'][patient][idp]

    def search_ref(self, dic_file, name_file):
        i=0
        for file_ref in self.dic_ref_files['filename']:
            if file_ref == name_file:
                return self.dic_ref_files['ref_var'][i]
            else :
                self.error_message = file_ref + ' no file in dic_ref_files'
            i+=1

        return ''

    def add_key_ref(self, key_var_file, patient, idp, ref):
        key_dic_file = self.list_key_ref[self.list_key_ref[key_var_file]['parentFileRef']]['listPatient'][patient][ref]
        try:
            key_dic_file[key_var_file][idp] ={}
            self.list_key_ref[key_var_file]['listPatient'][patient][idp] = key_dic_file[key_var_file][idp]
        except:
            key_dic_file[key_var_file] = {}
            key_dic_file[key_var_file][idp] ={}
            self.list_key_ref[key_var_file]['listPatient'][patient][idp] = key_dic_file[key_var_file][idp]

    def read_auto_val_patient(self) :
        f_read = open(self.file_PI, 'r')
        value = int(f_read.read())
        f_read.close()
        return value

    def update_val_patient(self):
        f_read = open(self.file_PI, 'w')
        f_read.write(str(self.patient_val))
        f_read.close()
