# -*- coding: utf-8 -*-
"""
Created 2018/01/05

@author: David BAUDOIN

fonction : script d'interaction avec la base de donnees i2b2

"""
from script_pivot_transfert.generate_pivot_json import PivotData
import pprint
import datetime
import re

class mapping_osiris:
    # construction de l'objet
    def __init__(self, obj_pivot, dic_metai2b2, source):
        self.obj_pivot = obj_pivot
        self.dic_metai2b2 = dic_metai2b2
        self.listvar = []
        self.default_date = datetime.date(2018, 9, 21)
        self.source = source

    def find_refvar_in_pivot (self, i2b2var):
        for refvar in self.obj_pivot.list_key_ref:
            #pprint.pprint(refvar)
            #print (self.obj_pivot.list_key_ref[refvar]['var'])
            if i2b2var.lower() in [x.lower() for x in self.obj_pivot.list_key_ref[refvar]['var']]: return refvar
        return None

    def find_matchvar_in_pivot (self, i2b2var):
        for refvar in self.obj_pivot.list_key_ref:
            for pivotvar in self.obj_pivot.list_key_ref[refvar]['var']:
                if i2b2var.lower() == pivotvar.lower():
                    return pivotvar
        return None

    def id_meta_var(self, var_ref, var):
        id_var = self.obj_pivot.list_key_ref[var_ref]['var']
        return id_var

    def transfert_patient_from_pivot (self, i2b2_var, patient, i2b2_concept_ref):
        dic_info = {}
        var_ref = self.find_refvar_in_pivot(i2b2_var)
        dic_info['date'] = self.default_date
        dic_info['table'] = 'concept_dimension'
        dic_info['visit_num'] = 0
        dic_info['provider_id'] = '@'
        dic_info['patient_num'] = self.obj_pivot.dic_patient[patient]
        dic_info['concept_cd'] = i2b2_concept_ref
        dic_info['modifier_cd'] = '@'
        dic_info['var'] = self.find_matchvar_in_pivot(i2b2_var)
        dic_info['instance_num'] = 1
        dic_info['nvalue'] = None
        try :
            dic_info['tvalue'] = self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][re.match('.*_', var_ref).group(0) + i2b2_var]
        except:
            dic_info['tvalue'] = None
        dic_info['sourcesystem_cd'] = self.source
        #self.listvar = [dic_info['tvalue'], dic_info['patient_num']]
        self.listvar = [dic_info['patient_num'], dic_info['visit_num'], dic_info['date'], dic_info['concept_cd'],
                        dic_info['tvalue'], dic_info['nvalue'], dic_info['date'], dic_info['modifier_cd'],
                        dic_info['instance_num'], dic_info['sourcesystem_cd'], dic_info['provider_id']]

        return dic_info

    def transfert_visit_from_pivot(self, i2b2_var, patient, visit, i2b2_concept_ref):
        dic_info = {}
        var_ref = self.find_refvar_in_pivot(i2b2_var)
        dic_info['date'] = self.default_date
        dic_info['modifier_cd'] = '@'
        dic_info['provider_id'] = '@'
        dic_info['instance_num'] = 1
        dic_info['var'] = self.find_matchvar_in_pivot(i2b2_var)
        dic_info['table'] = 'concept_dimension'
        dic_info['patient_num'] = self.obj_pivot.dic_patient[patient]
        dic_info['visit_num'] = visit
        #dic_info['concept_cd'] = self.find_matchvar_in_pivot(i2b2_var)
        dic_info['concept_cd'] = i2b2_concept_ref
        dic_info['sourcesystem_cd'] = self.source
        #pprint.pprint(self.obj_pivot.list_key_ref['TumorPathologyEvent_Ref']['listPatient']['L304'][visit][self.find_matchvar_in_pivot(i2b2_var)])
        try:
            #print(self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][visit])
            #print(re.match('.*_', var_ref).group(0) + i2b2_var)
            dic_info['tvalue'] = self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][visit][re.match('.*_', var_ref).group(0) + i2b2_var]
        except:
            dic_info['tvalue'] = None
        dic_info['nvalue'] = None
        #self.listvar = [dic_info['value'], dic_info['patient_num'], dic_info['visit_num']]
        self.listvar = [dic_info['patient_num'], dic_info['visit_num'], dic_info['date'], dic_info['concept_cd'],
                        dic_info['tvalue'], dic_info['nvalue'], dic_info['date'], dic_info['modifier_cd'],
                        dic_info['instance_num'], dic_info['sourcesystem_cd'], dic_info['provider_id']]
        return dic_info

    def transfert_concept_from_pivot(self, i2b2_var, patient, instance, i2b2_type, i2b2_basecode):
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
        dic_info['date'] = self.default_date
        dic_info['concept_cd'] = i2b2_basecode
        dic_info['modifier_cd'] = '@'
        dic_info['instance_num'] = 1
        dic_info['sourcesystem_cd'] = self.source
        dic_info['provider_id'] = '@'
        return dic_info


    def transfert_modifier_from_pivot(self, i2b2_var, patient, instance, i2b2_type, i2b2_basecode, i2b2_concept_ref):
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
        dic_info['date'] = self.default_date
        dic_info['concept_cd'] = i2b2_concept_ref
        dic_info['modifier_cd'] = i2b2_basecode
        dic_info['instance_num'] = instance
        dic_info['sourcesystem_cd'] = self.source
        dic_info['provider_id'] = '@'
        return dic_info