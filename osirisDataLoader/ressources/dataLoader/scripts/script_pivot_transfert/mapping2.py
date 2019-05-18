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
    def __init__(self, obj_pivot, dic_metai2b2, osiris_map, source):
        self.obj_pivot = obj_pivot
        self.dic_metai2b2 = dic_metai2b2
        #pprint.pprint(dic_metai2b2)
        self.listvar = []
        self.default_date = datetime.date(2018, 9, 21)
        self.osiris_map = osiris_map
        self.source = source
        self.instance_num = 0

    def find_refvar_in_pivot(self, i2b2var):
        for refvar in self.obj_pivot.list_key_ref:
            # print(i2b2var)
            # print(refvar)
            # pprint.pprint(self.obj_pivot.list_key_ref[refvar]['var'])
            # print (self.obj_pivot.list_key_ref[refvar]['var'])
            if i2b2var.lower() in [x.lower() for x in self.obj_pivot.list_key_ref[refvar]['var']]: return refvar
            elif i2b2var in self.obj_pivot.list_key_ref[refvar]['var']: return refvar
        return None

    def find_matchvar_in_pivot(self, i2b2var):
        for refvar in self.obj_pivot.list_key_ref:
            for pivotvar in self.obj_pivot.list_key_ref[refvar]['var']:
        #        print(i2b2var.lower() + ' ' + pivotvar.lower())
                if i2b2var.lower() == pivotvar.lower():
                    return pivotvar
        return None

    def id_meta_var(self, var_ref, var):
        id_var = self.obj_pivot.list_key_ref[var_ref]['var']
        return id_var

    def searchModalityID(self,i2b2_concept, mod):
        # if (i2b2_concept == "TumorPathologyEvent|MorphologyCode|ICDO3:8140/3"):
        #     print("searchModalityID ==> " +i2b2_concept)
        #     print(mod)
        try:
            concept_moda = re.findall('\|[^\|]*:[^\|\:]*', i2b2_concept)[0][1:] # fix regex for / to be accepted (ICDO3)
            # concept_moda = re.findall('\|[^\|]*:[a-zA-Z0-9]*', i2b2_concept)[0][1:]
        except:
            return None
        if(concept_moda == mod):
            print("===========================")
            print(i2b2_concept)
            print(concept_moda + " - " + mod)
            print(concept_moda == mod)
        if concept_moda == mod: return mod
        return None


    def transfert_data_element_concept_from_pivot(self, i2b2_var, patient, i2b2_concept, visit,mappings):
        dic_info = {}
        var_ref = i2b2_var + "_Ref"
        dic_info['date'] = self.match_date(mappings,var_ref,patient,visit,i2b2_concept,"Instance_Id","start_date")
        dic_info['end_date'] = self.match_date(mappings,var_ref,patient,visit,i2b2_concept,"Instance_Id","end_date")
        if dic_info['end_date'] == self.default_date:
            dic_info['end_date'] = dic_info['date']
        dic_info['table'] = 'concept_dimension'
        dic_info['visit_num'] = int(visit)
        dic_info['provider_id'] = '@'
        dic_info['patient_num'] = self.obj_pivot.dic_patient[patient]
        dic_info['modifier_cd'] = '@'
        dic_info['var'] = self.find_matchvar_in_pivot(i2b2_var)
        dic_info['instance_num'] = 1
        dic_info['nvalue'] = None
        dic_info['tvalue'] = i2b2_var
        dic_info['sourcesystem_cd'] = self.source
        dic_info['concept_cd'] = i2b2_var
        # print(dic_info['tvalue'])
        # self.listvar = [dic_info['tvalue'], dic_info['patient_num']]
        self.listvar = [dic_info['patient_num'], dic_info['visit_num'], dic_info['date'], dic_info['concept_cd'],
                        dic_info['tvalue'], dic_info['nvalue'], dic_info['date'], dic_info['modifier_cd'],
                        dic_info['instance_num'], dic_info['sourcesystem_cd'], dic_info['provider_id'],dic_info['end_date']]

        return dic_info
    def transfert_concept_from_pivot(self, i2b2_var, patient, i2b2_concept, visit):
        # print("concept-cd ==> " + i2b2_concept)
        # print("i2b2 var ==> " + i2b2_var)
        dic_info = {}
        var_ref = self.find_refvar_in_pivot(i2b2_var)
        dic_info['date'] = self.default_date
        dic_info['table'] = 'concept_dimension'
        dic_info['visit_num'] = int(visit)
        dic_info['provider_id'] = '@'
        dic_info['patient_num'] = self.obj_pivot.dic_patient[patient]
        dic_info['modifier_cd'] = '@'
        dic_info['var'] = self.find_matchvar_in_pivot(i2b2_var)
        dic_info['instance_num'] = 1
        dic_info['nvalue'] = None
        # print(i2b2_var[len(re.match('[a-zA-Z0-9]*\|', i2b2_var).group(0)):len(re.match('.*\|', i2b2_var).group(0))-1])
        # pprint.pprint(self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient])


        # print("__________________")
        # print(var_ref)
        # print(dic_info['var'])
        # pprint.pprint(self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][visit])
        # pprint.pprint(self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient])

        try:
            dic_info['tvalue'] = self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][visit][
                re.findall('.*_', var_ref)[0]+i2b2_var]
        except:
            dic_info['tvalue'] = None
        dic_info['sourcesystem_cd'] = self.source
        # print('tvalue ==> ')
        # print(dic_info['tvalue'])
        if dic_info['tvalue'] != None and ":" not in dic_info['tvalue'] : dic_info['tvalue'] = "os:"+dic_info['tvalue']
        if dic_info['tvalue'] != None: dic_info['tvalue'] = self.searchModalityID(i2b2_concept, dic_info['tvalue'])
        dic_info['concept_cd'] = i2b2_concept
        # print(dic_info['tvalue'])
        # self.listvar = [dic_info['tvalue'], dic_info['patient_num']]
        self.listvar = [dic_info['patient_num'], dic_info['visit_num'], dic_info['date'], dic_info['concept_cd'],
                        dic_info['tvalue'], dic_info['nvalue'], dic_info['date'], dic_info['modifier_cd'],
                        dic_info['instance_num'], dic_info['sourcesystem_cd'], dic_info['provider_id']]

        return dic_info


    def match_date(self, mappings, var_ref, patient, visit, i2b2_concept, i2b2_var, i2b2_column):
        data_element_concept= re.findall('^[^\|]*', i2b2_concept)[0]


        '''
        find the correct start_date in data matching concept and var.

        :param mappings: dict of mapping  {(concept,column): {'start_date': {value},'end_date': {value},'concept_modified': {value}}
        :param var_ref:
        :param patient:
        :param visit:
        :param i2b2_concept: concept in mapping (ex : Patient) */!\* REGEX needed
        :param i2b2_var: column in mapping (ex: LastNewsStatus)
        :param i2b2_column: current wanted column (ex: start_date)
        :return: the date of the start_date mapping column in data

        mappings[(re.findall('^[^\|]*', i2b2_concept)[0],i2b2_var)][i2b2_column]]] <==> dico[(concept,column)][start_date]
        '''
        try:
            if visit == '0':
                date = datetime.datetime.strptime(self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][
                                                      mappings[(data_element_concept, i2b2_var)][
                                                          data_element_concept+"_"+i2b2_column]], '%Y-%m-%d')
            else:
                target = data_element_concept+"_"+mappings[(data_element_concept, i2b2_var)][i2b2_column]
                if i2b2_var == 'Instance_Id':
                    print('======================================')
                    print(data_element_concept)
                    print(target)
                    print('********************')


                date = datetime.datetime.strptime(self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][visit][target], '%Y-%m-%d')
        except:
            date = self.default_date

        return date

    def match_instance_num(self, mappings, var_ref, patient, visit, i2b2_concept, i2b2_var, i2b2_column):
        '''
        find the correct start_date in data matching concept and var.

        :param mappings: dict of mapping  {(concept,column): {'start_date': {value},'end_date': {value},'concept_modified': {value}}
        :param var_ref:
        :param patient:
        :param visit:
        :param i2b2_concept: concept in mapping (ex : Patient) */!\* REGEX needed
        :param i2b2_var: column in mapping (ex: LastNewsStatus)
        :param i2b2_column: current wanted column (ex: start_date)
        :return: the date of the start_date mapping column in data

        mappings[(re.findall('^[^\|]*', i2b2_concept)[0],i2b2_var)][i2b2_column]]] <==> dico[(concept,column)][start_date]
        '''

        # pprint.pprint(mappings[(re.findall('^[^\|]*', i2b2_concept)[0], i2b2_var)][i2b2_column])
        # pprint.pprint(self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][visit])
        try:
            if visit == '0':
                isntance_num = self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][
                                                      mappings[(re.findall('^[^\|]*', i2b2_concept)[0], i2b2_var)][
                                                          i2b2_column]+'_Ref']
            else:
                if(mappings[(re.findall('^[^\|]*', i2b2_concept)[0], i2b2_var)][i2b2_column] != re.findall('^[^\|]*', i2b2_concept)[0]):
                    # pprint.pprint(self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][visit])
                    isntance_num = self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][visit][
                                                          mappings[(re.findall('^[^\|]*', i2b2_concept)[0], i2b2_var)][
                                                             i2b2_column]+'_Ref']
                else:
                    isntance_num = self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][visit]['Instance_Id']
        except:
            isntance_num = 0

        return isntance_num
    # def match_date(self,mappings,var_ref,patient,visit,i2b2_concept,i2b2_var,i2b2_column):
    #     date = self.default_date
    #     i = 0
    #     # print ("=====================")
    #     for concept in mappings['concept']:
    #         if concept == re.findall('^[^\|]*', i2b2_concept)[0]:
    #             if i2b2_var == mappings['column'][i]:
    #                 # print(i)
    #                 # print(i2b2_var)
    #                 # print( mappings['column'][i])
    #                 # print("==>  match")
    #                 # print(mappings['start_date'][i])
    #                 # pprint.pprint(datetime.datetime.strptime(self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][concept+"_"+mappings['start_date'][i]],'%Y-%m-%d'))
    #                 try:
    #                     if visit == '0':
    #                         date = datetime.datetime.strptime(self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][concept+"_"+mappings[i2b2_column][i]],'%Y-%m-%d')
    #                         # print(date)
    #                     else:
    #                         date = datetime.datetime.strptime(self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][visit][concept+"_"+mappings[i2b2_column][i]],'%Y-%m-%d')
    #                 except:
    #                     date = self.default_date
    #                 break
    #         i+= 1
    #
    #     return date



    def transfert_concept_from_pivot_with_mappings(self, i2b2_var, patient, i2b2_concept, visit,mappings):
        # if (i2b2_concept == "TumorPathologyEvent|MorphologyCode|ICDO3:8140/3"):
        #     print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        #     print("concept-cd ==> " + i2b2_concept)
        #     print("i2b2 var ==> " + i2b2_var)

        dic_info = {}
        var_ref = self.find_refvar_in_pivot(i2b2_var)
        dic_info['date'] = self.match_date(mappings,var_ref,patient,visit,i2b2_concept,i2b2_var,"start_date")
        dic_info['end_date'] = self.match_date(mappings,var_ref,patient,visit,i2b2_concept,i2b2_var,"end_date")
        if dic_info['end_date'] == self.default_date:
            dic_info['end_date'] = dic_info['date']
        dic_info['table'] = 'concept_dimension'
        dic_info['visit_num'] = int(visit)
        dic_info['provider_id'] = '@'
        dic_info['patient_num'] = self.obj_pivot.dic_patient[patient]
        dic_info['modifier_cd'] = '@'
        dic_info['var'] = self.find_matchvar_in_pivot(i2b2_var)
        dic_info['instance_num'] = self.instance_num
        dic_info['nvalue'] = None
        # print(i2b2_var[len(re.match('[a-zA-Z0-9]*\|', i2b2_var).group(0)):len(re.match('.*\|', i2b2_var).group(0))-1])
        # pprint.pprint(self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient])

        # if (i2b2_concept == "TumorPathologyEvent|MorphologyCode|ICDO3:8140/3"):
        #     print("__________________")
        #     print(var_ref)
        #     print(dic_info['var'])
        #     pprint.pprint(self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][visit])
        #     pprint.pprint(self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient])

        try:
            dic_info['tvalue'] = self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][visit][
                re.findall('.*_', var_ref)[0]+i2b2_var]
        except:
            dic_info['tvalue'] = None
        dic_info['sourcesystem_cd'] = self.source
        # if (i2b2_concept == "TumorPathologyEvent|MorphologyCode|ICDO3:8140/3"):
        #     print('tvalue ==> ')
        #     print(dic_info['tvalue'])
        if dic_info['tvalue'] != None and ":" not in dic_info['tvalue'] : dic_info['tvalue'] = "os:"+dic_info['tvalue']
        # if (i2b2_concept == "TumorPathologyEvent|MorphologyCode|ICDO3:8140/3"):
        #     print(dic_info['tvalue'])
        if dic_info['tvalue'] != None: dic_info['tvalue'] = self.searchModalityID(i2b2_concept, dic_info['tvalue'])
        dic_info['concept_cd'] = i2b2_concept
        # if (i2b2_concept == "TumorPathologyEvent|MorphologyCode|ICDO3:8140/3"):
        #     print("BBBBBBBBBBBBBBBBBBBBB")
        #     print(dic_info['tvalue'])
        #     print(dic_info['concept_cd'])
        # self.listvar = [dic_info['tvalue'], dic_info['patient_num']]
        self.listvar = [dic_info['patient_num'], dic_info['visit_num'], dic_info['date'], dic_info['concept_cd'],
                        dic_info['tvalue'], dic_info['nvalue'], dic_info['date'], dic_info['modifier_cd'],
                        dic_info['instance_num'], dic_info['sourcesystem_cd'], dic_info['provider_id'],dic_info['end_date']]

        return dic_info

    def transfert_patient_from_pivot(self, i2b2_var, patient, i2b2_concept_ref):
        dic_info = {}
        # print(i2b2_var)
        var_ref = self.find_refvar_in_pivot(i2b2_var)
        dic_info['date'] = self.default_date
        dic_info['table'] = 'concept_dimension'
        dic_info['visit_num'] = 0
        dic_info['provider_id'] = '@'
        dic_info['patient_num'] = self.obj_pivot.dic_patient[patient]
        dic_info['modifier_cd'] = '@'
        dic_info['var'] = self.find_matchvar_in_pivot(i2b2_var)
        dic_info['instance_num'] = 1
        dic_info['nvalue'] = None
        #print(i2b2_var[len(re.match('[a-zA-Z0-9]*\|', i2b2_var).group(0)):len(re.match('.*\|', i2b2_var).group(0))-1])
        #pprint.pprint(self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient])
        try:
            dic_info['tvalue'] = self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][
                'Patient_' + i2b2_var]
        except:
            dic_info['tvalue'] = None
        dic_info['sourcesystem_cd'] = self.source
        # print('tvalue ==> ')
        # print(dic_info['tvalue'])
        if dic_info['tvalue'] != None: dic_info['tvalue'] = self.searchModalityID(i2b2_concept_ref, dic_info['tvalue'])
        dic_info['concept_cd'] = i2b2_concept_ref
        #print(dic_info['tvalue'])
        # self.listvar = [dic_info['tvalue'], dic_info['patient_num']]
        self.listvar = [dic_info['patient_num'], dic_info['visit_num'], dic_info['date'], dic_info['concept_cd'],
                        dic_info['tvalue'], dic_info['nvalue'], dic_info['date'], dic_info['modifier_cd'],
                        dic_info['instance_num'], dic_info['sourcesystem_cd'], dic_info['provider_id']]

        return dic_info

    def transfert_patient_from_pivot_with_mappings(self, i2b2_var, patient, i2b2_concept_ref,mappings):
        dic_info = {}
        # print(i2b2_var)
        self.instance_num += 1
        var_ref = self.find_refvar_in_pivot(i2b2_var)
        dic_info['date'] = self.match_date(mappings,var_ref,patient,'0',i2b2_concept_ref,i2b2_var,'start_date')
        dic_info['end_date'] = self.match_date(mappings,var_ref,patient,'0',i2b2_concept_ref,i2b2_var,"end_date")
        if dic_info['end_date'] == self.default_date:
            dic_info['end_date'] = dic_info['date']
        dic_info['table'] = 'concept_dimension'
        dic_info['visit_num'] = 0
        dic_info['provider_id'] = '@'
        dic_info['patient_num'] = self.obj_pivot.dic_patient[patient]
        dic_info['modifier_cd'] = '@'
        dic_info['var'] = self.find_matchvar_in_pivot(i2b2_var)
        dic_info['instance_num'] = self.instance_num
        dic_info['nvalue'] = None
        #print(i2b2_var[len(re.match('[a-zA-Z0-9]*\|', i2b2_var).group(0)):len(re.match('.*\|', i2b2_var).group(0))-1])
        #pprint.pprint(self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient])
        try:
            dic_info['tvalue'] = self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][
                'Patient_' + i2b2_var]
        except:
            dic_info['tvalue'] = None
        dic_info['sourcesystem_cd'] = self.source
        # print('tvalue ==> ')
        # print(dic_info['tvalue'])
        if dic_info['tvalue'] != None: dic_info['tvalue'] = self.searchModalityID(i2b2_concept_ref, dic_info['tvalue'])
        dic_info['concept_cd'] = i2b2_concept_ref
        print(dic_info['tvalue'])
        # self.listvar = [dic_info['tvalue'], dic_info['patient_num']]
        self.listvar = [dic_info['patient_num'], dic_info['visit_num'], dic_info['date'], dic_info['concept_cd'],
                        dic_info['tvalue'], dic_info['nvalue'], dic_info['date'], dic_info['modifier_cd'],
                        dic_info['instance_num'], dic_info['sourcesystem_cd'], dic_info['provider_id'],dic_info['end_date']]
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
        # dic_info['concept_cd'] = self.find_matchvar_in_pivot(i2b2_var)
        dic_info['sourcesystem_cd'] = self.source
        # pprint.pprint(self.obj_pivot.list_key_ref['TumorPathologyEvent_Ref']['listPatient']['L304'][visit][self.find_matchvar_in_pivot(i2b2_var)])
        try:
            # print(self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][visit])
            # print(re.match('.*_', var_ref).group(0) + i2b2_var)
            dic_info['tvalue'] = self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][visit][
                i2b2_var]
        except:
            dic_info['tvalue'] = None
        dic_info['nvalue'] = None
        # self.listvar = [dic_info['value'], dic_info['patient_num'], dic_info['visit_num']]
        concept_moda = self.searchModalityID(i2b2_concept_ref, dic_info['tvalue'])
        if concept_moda != None:
            dic_info['concept_cd'] = concept_moda
        else:
            dic_info['concept_cd'] = i2b2_concept_ref
        self.listvar = [dic_info['patient_num'], dic_info['visit_num'], dic_info['date'], dic_info['concept_cd'],
                        dic_info['tvalue'], dic_info['nvalue'], dic_info['date'], dic_info['modifier_cd'],
                        dic_info['instance_num'], dic_info['sourcesystem_cd'], dic_info['provider_id']]
        return dic_info


    def transfert_modifier_from_pivot(self, i2b2_var, patient, i2b2_modifier, visit, instance, i2b2_concept_ref,mappings):
        # print('i2b2_modifeir ==> ' + i2b2_modifier)
        # print('i2b2_var ==> ' + i2b2_var)
        # print(re.findall('\|([^\|]*)', i2b2_var)[0])
        # pprint.pprint(mappings)

        dic_info = {}
        var_ref = re.findall('^[^\|]*',i2b2_modifier)[0]+"_Ref"
        #TODO : La date peut se trouver dans un autre concept
        #TODO :(date pour drug = start_date du traitement)
        #TODO : il suffit d'envoyer le bon i2b2_concept à la place de re.findall('\|([^\|]*)', i2b2_var)[0]
        dic_info['date'] = self.match_date(mappings,var_ref,patient,visit,i2b2_var,re.findall('\|([^\|]*)', i2b2_var)[0],"start_date")
        dic_info['end_date'] = self.match_date(mappings,var_ref,patient,visit,i2b2_var,re.findall('\|([^\|]*)', i2b2_var)[0],"end_date")
        if dic_info['end_date'] == self.default_date:
            dic_info['end_date'] = dic_info['date']
        dic_info['table'] = 'concept_dimension'
        dic_info['visit_num'] = int(visit)
        dic_info['provider_id'] = '@'
        dic_info['patient_num'] = self.obj_pivot.dic_patient[patient]
        dic_info['modifier_cd'] = i2b2_var
        dic_info['var'] = self.find_matchvar_in_pivot(i2b2_var)

        dic_info['instance_num'] = self.match_instance_num(mappings,var_ref,patient,instance,i2b2_var,re.findall('\|([^\|]*)', i2b2_var)[0],"concept_modified")
        dic_info['nvalue'] = None

        # pprint.pprint(self.obj_pivot.list_key_ref[var_ref][patient][instance])
        # if (re.findall('^[^\|]*', i2b2_var)[0]+"_"+re.findall('\|([^\|]*)', i2b2_var)[0] == 'Treatment_Type'):
        #     print("*******************************")
        #     print(re.findall('^[^\|]*', i2b2_var)[0]+"_"+re.findall('\|([^\|]*)', i2b2_var)[0])
            # print(var_ref)
            # pprint.pprint(self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][instance])
        try:
            dic_info['tvalue'] = self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][instance][
                re.findall('^[^\|]*', i2b2_var)[0]+"_"+re.findall('\|([^\|]*)', i2b2_var)[0]]
            # if (re.findall('^[^\|]*', i2b2_var)[0]+"_"+re.findall('\|([^\|]*)', i2b2_var)[0] == 'Treatment_Type'):
            #     pprint.pprint(self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][instance][
            #     re.findall('^[^\|]*', i2b2_var)[0]+"_"+re.findall('\|([^\|]*)', i2b2_var)[0]])
        except:
            dic_info['tvalue'] = None
        dic_info['sourcesystem_cd'] = self.source
        # print('tvalue ==> ')

        # print('ref ==> ' + i2b2_modifier)
        if dic_info['tvalue'] != None and ":" not in dic_info['tvalue'] : dic_info['tvalue'] = "os:"+dic_info['tvalue']
        if dic_info['tvalue'] != None : dic_info['tvalue'] = self.searchModalityID(i2b2_modifier, dic_info['tvalue'])

        try:
            dic_info['concept_cd'] = mappings[re.findall('^[^\|]*', i2b2_var)[0],re.findall('\|([^\|]*)', i2b2_var)[0]]['concept_modified']

        except:
            # pprint.pprint(mappings[re.findall('^[^\|]*', i2b2_var)[0],re.findall('\|([^\|]*)', i2b2_var)[0]])
            dic_info['concept_cd'] = None
            dic_info['tvalue'] = None

        if (dic_info['tvalue'] != None):
            pprint.pprint(dic_info)
        # try:
        #     dic_info['tvalue'] = self.obj_pivot.list_key_ref[var_ref]['listPatient'][patient][
        #         'Patient_' + i2b2_var[
        #                      len(re.match('[a-zA-Z0-9]*\|', i2b2_var).group(0)):len(
        #                          re.match('.*\|', i2b2_var).group(0)) - 1]]
        # except:
        #     dic_info['tvalue'] = None
        # dic_info['sourcesystem_cd'] = self.source
        # if dic_info['tvalue'] != None: dic_info['tvalue'] = self.searchModalityID(i2b2_var, dic_info['tvalue'])
        # dic_info['concept_cd'] = i2b2_concept_ref
        # print(dic_info['tvalue'])
        # self.listvar = [dic_info['tvalue'], dic_info['patient_num']]
        self.listvar = [dic_info['patient_num'], dic_info['visit_num'], dic_info['date'], dic_info['concept_cd'],
                        dic_info['tvalue'], dic_info['nvalue'], dic_info['date'], dic_info['modifier_cd'],
                        dic_info['instance_num'], dic_info['sourcesystem_cd'], dic_info['provider_id'],dic_info['end_date']]

        return dic_info
