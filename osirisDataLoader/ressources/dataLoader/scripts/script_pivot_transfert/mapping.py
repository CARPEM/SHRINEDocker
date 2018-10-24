# -*- coding: utf-8 -*-
"""
Created 2018/01/05

@author: David BAUDOIN

fonction : script d'interaction avec la base de donnees i2b2

"""
from script_pivot_transfert.generate_pivot_json import PivotData
import pprint
import datetime

class mapping_osiris:
    # construction de l'objet
    def __init__(self, obj_pivot, dic_metai2b2):
        self.obj_pivot = obj_pivot
        self.dic_metai2b2 = dic_metai2b2
        self.listvar = []

    def find_refvar_in_pivot (self, i2b2var):
        for refvar in self.obj_pivot.list_key_ref:
            #pprint.pprint(i2b2var)
            #print (self.obj_pivot.list_key_ref[refvar]['var'])
            if i2b2var.lower() in [x.lower() for x in self.obj_pivot.list_key_ref[refvar]['var']]: return refvar
        return None

    def find_matchvar_in_pivot (self, i2b2var):
        for refvar in self.obj_pivot.list_key_ref:
            for pivotvar in self.obj_pivot.list_key_ref[refvar]['var']:
                if i2b2var.lower() == pivotvar.lower():
                    return pivotvar
        return None

    def transfert_patient_from_pivot (self, i2b2_var, patient):
        dic_info = {}
        var_ref = self.find_refvar_in_pivot(i2b2_var)
        dic_info['table'] = 'patient_dimension'
        dic_info['patient_num'] = self.obj_pivot.dic_patient[patient]
        dic_info['var'] = i2b2_var
        dic_info['value'] = self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][i2b2_var]
        dic_info['sourcesystem_cd'] = 'TEST_OSIRIS'
        self.listvar = [dic_info['value'], dic_info['patient_num']]

        return dic_info

    def transfert_visit_from_pivot(self, i2b2_var, patient, visit):
        dic_info = {}
        var_ref = self.find_refvar_in_pivot(i2b2_var)
        dic_info['table'] = 'visit_dimension'
        dic_info['patient_num'] = self.obj_pivot.dic_patient[patient]
        dic_info['encounter_num'] = visit
        dic_info['var'] = self.find_matchvar_in_pivot(i2b2_var)
        dic_info['sourcesystem_cd'] = 'TEST_OSIRIS'
        #pprint.pprint(self.obj_pivot.list_key_ref['TumorPathologyEvent_Ref']['listPatient']['L304'][visit][self.find_matchvar_in_pivot(i2b2_var)])
        try:
            dic_info['value'] = self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][visit][self.find_matchvar_in_pivot(i2b2_var)]
        except:
            dic_info['value'] = None
        self.listvar = [dic_info['value'], dic_info['patient_num'], dic_info['encounter_num']]
        return dic_info

    def transfert_concept_from_pivot(self, i2b2_var, patient, instance, i2b2_type):
        dic_info = {}
        var_ref = self.find_refvar_in_pivot(i2b2_var)
        dic_info['patient_num'] = self.obj_pivot.dic_patient[patient]
        dic_info['encounter_num'] = self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][instance]['TumorPathologyEvent_Ref']
        dic_info['var'] = i2b2_var
        if i2b2_type == 'N':
            try:
                dic_info['nvalue'] = float(self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][instance][self.find_matchvar_in_pivot(i2b2_var)])
                dic_info['tvalue'] = 'E'
            except :
                dic_info['nvalue'] = None
                dic_info['tvalue'] = None
        else:
            dic_info['nvalue'] = None
            try:
                dic_info['value'] = self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][instance][self.find_matchvar_in_pivot(i2b2_var)]
            except:
                dic_info['tvalue'] = None

        # changer pour la commande now
        dic_info['date'] = datetime.date(2018, 9, 21)
        dic_info['concept_cd'] = i2b2_var
        dic_info['modifier_cd'] = '@'
        dic_info['instance_num'] = 1
        dic_info['sourcesystem_cd'] = 'TEST_OSIRIS'
        dic_info['provider_id'] = '@'
        return dic_info


    def transfert_modifier_from_pivot(self, i2b2_var, patient, instance, i2b2_type):
        dic_info = {}
        var_ref = self.find_refvar_in_pivot(i2b2_var)
        dic_info['patient_num'] = self.obj_pivot.dic_patient[patient]
        dic_info['encounter_num'] = self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][instance]['TumorPathologyEvent_Ref']
        dic_info['var'] = i2b2_var
        if i2b2_type == 'n':
            try:
                dic_info['nvalue'] = float(self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][instance][self.find_matchvar_in_pivot(i2b2_var)])
                dic_info['tvalue'] = 'E'
            except:
                dic_info['nvalue'] = None
                dic_info['tvalue'] = None
        else:
            dic_info['nvalue'] = None
            try:
                dic_info['tvalue'] = self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][instance][self.find_matchvar_in_pivot(i2b2_var)]
            except:
                dic_info['tvalue'] = None

        # changer pour la commande now
        dic_info['date'] = datetime.date(2018, 9, 21)
        dic_info['concept_cd'] = i2b2_var
        dic_info['modifier_cd'] = i2b2_var
        dic_info['instance_num'] = 1
        dic_info['sourcesystem_cd'] = 'TEST_OSIRIS'
        dic_info['provider_id'] = '@'
        return dic_info