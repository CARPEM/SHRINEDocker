# -*- coding: utf-8 -*-
"""
Created 2018/05/28

@author: david
script de transfert des donnees issu du pivot vers la base de donnees i2b2
"""
import re, sys, pprint, os
from script_pivot_transfert.lect_file import lecture_csv_file
from script_pivot_transfert.generate_pivot_json import PivotData
from script_pivot_transfert.SQLexecution import i2b2_interaction
from script_pivot_transfert.mapping2 import mapping_osiris
from script_pivot_transfert.request import SQL_request


def search_basecode (var, list_ref):
    i=0
    #if var == 'T': print('recherche de la vaiable TNM_T')
    for ref in list_ref['var_pivot'] :
        #if var == 'T': print(ref)
        try :
            ref_match = ref[len(re.match('.*_', ref).group(0)):]
        except:
            ref_match = ref
        if var == ref_match:
            #print('find : ' + list_ref['basecode_i2b2'][i])
            return list_ref['basecode_i2b2'][i]
        i += 1
    return ''

def download_pivot_file(dic_db_param, dic_pivot_files):
    # create jsonfile base
    patients = lecture_csv_file(dic_pivot_files['patient'], ',')
    visites = lecture_csv_file(dic_pivot_files['visit'], ',')
    ref_files = lecture_csv_file(dic_pivot_files['dep_files'], ';')
    dic_patient = patients.copy_csv_file()

    dic_visit = visites.copy_csv_file()
    dic_ref_files = ref_files.copy_csv_file()
    pivot = PivotData('Patient_Id', 'TumorPathologyEvent_Ref', 'Instance_Id', dic_ref_files,
                      dic_pivot_files['incre_patient'], 'TEST_OSIRIS')
    pivot.add_patient_dimension(dic_patient, dic_db_param)
    pivot.add_visit_dimension(dic_visit, dic_db_param)

    '''
    # add biological sample
    BioSample = lecture_csv_file(dic_pivot_files['BioSample'], ',')
    dic_BioSample = BioSample.copy_csv_file()
    pivot.add_file_into_data(dic_BioSample, 'OSIRIS_pivot_BiologicalSample.csv')

    # add Analysis
    Analysis = lecture_csv_file(dic_pivot_files['Analysis'], ',')
    dic_Analysis = Analysis.copy_csv_file()
    pivot.add_file_into_data(dic_Analysis, 'OSIRIS_pivot_Analysis.csv')

    # add BioMarker
    BioMarker = lecture_csv_file(dic_pivot_files['BioMarker'], ',')
    dic_BioMarker = BioMarker.copy_csv_file()
    pivot.add_file_into_data(dic_BioMarker, 'OSIRIS_pivot_Biomarker.csv')

    # add Consent
    Consent = lecture_csv_file(dic_pivot_files['Consent'], ',')
    dic_Consent = Consent.copy_csv_file()
    pivot.add_file_into_data(dic_Consent, 'OSIRIS_pivot_Consent.csv')
    '''

    # add all file in pivot_files (all file who is reading is indicating in ref_files)
    list_file = lecture_csv_file(dic_pivot_files['dep_files'], ';')
    dic_listfiles = list_file.copy_csv_file()
    for file in list_file.dic_data['filename'][2:]:
        print(os.listdir(dic_db_param['path_to_data']))
        dic_files = {}
        if file in os.listdir(dic_db_param['path_to_data']):
            print(file)
            dataFile = lecture_csv_file(dic_db_param['path_to_data'] + file, ',')
            dic_files = dataFile.copy_csv_file()
            pivot.add_file_into_data(dic_files, file)
        else: break

    # pprint.pprint(pivot.list_key_ref)
    return pivot


def load_i2b2_metadata(dic_db_param, sql_file):
    dic_i2b2_metadata = {}
    dic_i2b2_metadata['file'] = []
    dic_i2b2_metadata['column'] = []
    dic_i2b2_metadata['type_var_i2b2'] = []
    dic_i2b2_metadata['id_modality'] = []
    dic_i2b2_metadata['concept_cd'] = []

    # create a connexion between i2b2 database
    interac_i2b2 = i2b2_interaction(dic_db_param['DB_type'], dic_db_param['DB_host'], dic_db_param['DB_name'],
                                    dic_db_param['DB_port'], dic_db_param['BD_user'], dic_db_param['DB_password'])

    # execute select metadata request
    sql_take_i2b2_metadata = open(dic_db_param['path_to_scripts'] + sql_file, 'r')
    tab_metadata = interac_i2b2.executeBasicRequest_n(sql_take_i2b2_metadata.read(), 2)

    # transfert result to tab_metadata
    for metadata in tab_metadata:
        #print(metadata)
        dic_i2b2_metadata['file'].append(metadata[0].split('|')[0])
        dic_i2b2_metadata['column'].append(metadata[0].split('|')[1])
        try:
            dic_i2b2_metadata['id_modality'].append(metadata[0].split('|')[2])
        except:
            dic_i2b2_metadata['id_modality'].append("")
        dic_i2b2_metadata['type_var_i2b2'].append('T')
        dic_i2b2_metadata['concept_cd'].append(metadata[0])
    return dic_i2b2_metadata

def match_i2b2_metadata_with_dic_pivot(pivot, concept_to_transfert, modifier_to_transfert, outputfile, logfile,
                                       dic_db_param, dic_pivot_files,mappings):
    i = 0
    f_output = open(outputfile, 'w')
    #pprint.pprint(pivot.dicData)

    req = SQL_request()
    interac_i2b2 = i2b2_interaction(dic_db_param['DB_type'], dic_db_param['DB_host'], dic_db_param['DB_name'],
                                    dic_db_param['DB_port'], dic_db_param['BD_user'], dic_db_param['DB_password'])

    # cas concept (patient et visit)
    metadata_file = lecture_csv_file(dic_pivot_files['metadata_file'], ';')
    dic_metadata_file = metadata_file.copy_csv_file()
    # pprint.pprint(pivot.list_key_ref)
    # pprint.pprint(concept_to_transfert['concept_cd'])
    obj_mapping = mapping_osiris(pivot, concept_to_transfert, dic_metadata_file, dic_db_param['source'])

    data_element_concept_transfered = {}
    for metadata in concept_to_transfert['concept_cd']:

        # print("add" + re.findall('^[^\|]*',concept_to_transfert['concept_cd'][i])[0])

        data_element_concept = re.findall('^[^\|]*', concept_to_transfert['concept_cd'][i])[0]
        if data_element_concept not in data_element_concept_transfered:
            data_element_concept_transfered[re.findall('^[^\|]*', concept_to_transfert['concept_cd'][i])[0]] = "tranfered"
            print("To add ====>" + data_element_concept)
            print(concept_to_transfert['column'][i])
            if data_element_concept != 'Patient':
            # and data_element_concept != 'TumorPathologyEvent':
                link_map_data =  data_element_concept + "_Ref"
                try:
                    for patient in pivot.list_key_ref[link_map_data]['listPatient']:
                        for visit in pivot.list_key_ref[link_map_data]['listPatient'][patient]:
                            i2b2_var = data_element_concept
                            i2b2_concept_ref = data_element_concept
                            dic_data_spe = obj_mapping.transfert_data_element_concept_from_pivot(i2b2_var, patient, i2b2_concept_ref, visit,mappings)
                            if dic_data_spe['tvalue'] != None or dic_data_spe['nvalue'] != None:
                                interac_i2b2.insert_data(req.write_insert_i2b2_data(dic_data_spe), obj_mapping.listvar)
                except:
                    print("nothing to do")
        try:
            i2b2_var = concept_to_transfert['column'][i]
            i2b2_table_cible = concept_to_transfert['file'][i]
            i2b2_type = concept_to_transfert['type_var_i2b2'][i]
            i2b2_concept_ref = concept_to_transfert['concept_cd'][i]
            # search data info from metadata
            link_map_data = obj_mapping.find_refvar_in_pivot(concept_to_transfert['column'][i])

        except Exception as e:
            link_map_data = None
            print(e)

        # pprint.pprint(link_map_data)
        # pprint.pprint(i2b2_table_cible)
        # pprint.pprint(i2b2_type)

        if link_map_data != None:
            # print("link ====> " + link_map_data)
            for patient in pivot.list_key_ref[link_map_data]['listPatient']:

                # select all data needed
                if i2b2_table_cible.lower() == 'patient':
                    dic_data_spe = obj_mapping.transfert_patient_from_pivot_with_mappings(i2b2_var, patient, i2b2_concept_ref,mappings)
                    # print(dic_data_spe)
                    # build insert request
                    if dic_data_spe['tvalue'] != None or dic_data_spe['nvalue'] != None :
                        interac_i2b2.insert_data(req.write_insert_i2b2_data(dic_data_spe), obj_mapping.listvar)
                    # copy resquest to outputfile
                    # f_output.writelines(req.write_insert_i2b2_data(dic_data_spe))

                else:
                    # pprint.pprint(pivot.list_key_ref[link_map_data]['listPatient'][patient])
                    for visit in pivot.list_key_ref[link_map_data]['listPatient'][patient]:
                        dic_data_spe = obj_mapping.transfert_concept_from_pivot_with_mappings(i2b2_var, patient, i2b2_concept_ref, visit,mappings)
                        # pprint.pprint(dic_data_spe)
                        if dic_data_spe['tvalue'] != None or dic_data_spe['nvalue'] != None:
                            interac_i2b2.insert_data(req.write_insert_i2b2_data(dic_data_spe), obj_mapping.listvar)
                        # add cas tumorPathologyEvent
                        # if i2b2_table_cible == 'tumorPathologyEvent':
                        #     dic_data_spe['table'] = 'visit_dimension'
                        #     interac_i2b2.insert_data(req.write_insert_i2b2_data(dic_data_spe),
                        #                              [dic_data_spe['tvalue'], dic_data_spe['patient_num'],
                        #                               dic_data_spe['visit_num']])

        i += 1

    # cas modifier
    '''    '''

    i = 0

    for metadata in modifier_to_transfert['concept_cd']:
        data_element_concept = re.findall('^[^\|]*', modifier_to_transfert['concept_cd'][i])[0]
        if data_element_concept not in data_element_concept_transfered:
            data_element_concept_transfered[re.findall('^[^\|]*', modifier_to_transfert['concept_cd'][i])[0]] = "tranfered"
            print("To add ====>" + data_element_concept)
            # print(modifier_to_transfert['column'][i])
            if data_element_concept != 'Patient':
            # and data_element_concept != 'TumorPathologyEvent':
                link_map_data =  data_element_concept + "_Ref"
                try:
                    for patient in pivot.list_key_ref[link_map_data]['listPatient']:
                        for visit in pivot.list_key_ref[link_map_data]['listPatient'][patient]:
                            i2b2_var = data_element_concept
                            i2b2_concept_ref = data_element_concept
                            dic_data_spe = obj_mapping.transfert_data_element_concept_from_pivot(i2b2_var, patient, i2b2_concept_ref, visit,mappings)
                            if dic_data_spe['tvalue'] != None or dic_data_spe['nvalue'] != None:
                                interac_i2b2.insert_data(req.write_insert_i2b2_data(dic_data_spe), obj_mapping.listvar)
                except:
                    print("Nothing To do")
        try:
            if (modifier_to_transfert['column'][i] == 'Type'):
                print("***********************=========================================>" +modifier_to_transfert['concept_cd'][i])
            i2b2_var = metadata
            i2b2_table_cible = modifier_to_transfert['file'][i]
            i2b2_type = modifier_to_transfert['type_var_i2b2'][i]
            # ici modifier_cd = concept_cd
            i2b2_modifier_ref = modifier_to_transfert['concept_cd'][i]
            # search data info from metadata
            link_map_data = re.findall('^[^\|]*',i2b2_modifier_ref)[0]+"_Ref"
            # link_map_data = obj_mapping.find_refvar_in_pivot(modifier_to_transfert['column'][i])
        except Exception as e:
            print(e)
            print(i2b2_var)
            pprint.pprint(modifier_to_transfert['column'][i])
            link_map_data = None

        if link_map_data != None:
            # print('**************************')
            # print(metadata)
            # print(concept_to_transfert['file'][i])
            # print(concept_to_transfert['type_var_i2b2'][i])
            # print(concept_to_transfert['column'][i])
            # print('**************************')
            try:

                for patient in pivot.list_key_ref[link_map_data]['listPatient']:
                    for instance in pivot.list_key_ref[link_map_data]['listPatient'][patient]:
                        if link_map_data == "TumorPathologyEvent_Ref":
                            visit = instance
                        else:
                            if link_map_data == "Patient_Ref":
                                visit = 0
                            else:
                                visit = pivot.list_key_ref[link_map_data]['listPatient'][patient][instance]['TumorPathologyEvent_Ref']

                        # print(i2b2_var)
                        # print(patient)
                        # print(i2b2_modifier_ref)
                        # print(visit)
                        # print(instance)
                        # i2b2_var, patient, i2b2_modifier, visit, instance, i2b2_concept_ref
                        # print('************************')
                        # print(i2b2_var)
                        # print(patient)
                        # print(i2b2_modifier_ref)
                        # print(visit)
                        # print(instance)
                        # pprint.pprint(pivot.list_key_ref[link_map_data]['listPatient'][patient][instance])
                        # visit = pivot.list_key_ref[link_map_data]['listPatient'][patient][instance]['TumorPathologyEvent_Ref']
                        dic_data_spe = obj_mapping.transfert_modifier_from_pivot(i2b2_var, patient, i2b2_modifier_ref, visit, instance, 'concept_to_define',mappings)
                        # if link_map_data == 'Treatment_Ref':
                        #     pprint.pprint("************=====")
                        #     pprint.pprint(instance)
                        #     pprint.pprint(pivot.list_key_ref[link_map_data]['listPatient'][patient][instance])

                        if dic_data_spe['tvalue'] != None or dic_data_spe['nvalue'] != None:
                            interac_i2b2.insert_data(req.write_insert_i2b2_data(dic_data_spe), obj_mapping.listvar)
            except Exception as e:
                print(e)
                print(link_map_data)
        i += 1
    f_output.close()
    # pprint.pprint(pivot.list_key_ref)


def tranfo_data(dic_db_param, dic_pivot_files):
    # create json file
    pivot = download_pivot_file(dic_db_param, dic_pivot_files)
    # pprint.pprint(pivot.dicData)
    # print(pivot.dicData['L304']['TumorPathologyEvent_Ref']['2']['BiologicalSample_Ref'])
    # pprint.pprint(pivot.list_key_ref['Analysis_Ref']['listPatient'])
    # pprint.pprint(pivot.list_key_ref['TumorPathologyEvent_Ref']['listPatient'])

    # import i2b2 metadata file
    mappings_file = lecture_csv_file(dic_pivot_files['mappings_file'] ,',')
    #à produire mappings ++++
    # mappings = mappings_file.copy_csv_file()
    mappings = mappings_file.copy_csv_to_dict_tuple_index()

    concept_to_transfert = load_i2b2_metadata(dic_db_param, dic_db_param['concept_sql'])
    modifier_to_transfert = load_i2b2_metadata(dic_db_param, dic_db_param['modifier_sql'])

    # pprint.pprint(metadata_to_transfert)

    # map i2b2 metadata to json file
    match_i2b2_metadata_with_dic_pivot(pivot, concept_to_transfert, modifier_to_transfert, dic_db_param['output_file'],
                                       dic_db_param['log_file'], dic_db_param, dic_pivot_files,mappings)

    # print(metadata_to_transfert)

def main():

    path_to_scripts='/opt/dataLoader/scripts/'
    path_to_data='/opt/data_to_load/'
    path_to_mapping = '/opt/mapping_files/'
    # DB parameters
    dic_db_param = {}
    dic_db_param['DB_host'] = os.environ['I2B2_DB_HOST']
    dic_db_param['DB_name'] = os.environ['POSTGRES_DB']
    dic_db_param['DB_port'] = os.environ['I2B2_DB_PORT']
    dic_db_param['BD_user'] = os.environ['POSTGRES_USER']
    dic_db_param['DB_password'] = os.environ['POSTGRES_PASSWORD']
    dic_db_param['DB_type'] = os.environ['SERVER_TYPE']
    dic_db_param['path_to_scripts'] = path_to_scripts
    dic_db_param['path_to_data'] = path_to_data
    dic_db_param['patvis_sql'] = 'select_i2b2_metadata.sql'
    dic_db_param['conceptmodif_sql'] = 'select_concept_modif_id.sql'
    dic_db_param['modifier_sql'] = 'select_all_modifier_OSIRIS.sql'
    dic_db_param['concept_sql'] = 'select_all_concept_OSIRIS.sql'
    dic_db_param['concept_link'] = 'select_link_concept_OSIRIS.sql'
    dic_db_param['output_file'] = 'osiris_test_logfile.csv'
    dic_db_param['log_file'] = 'osiris_test_output.csv'
    dic_db_param['source'] = 'TEST_OSIRIS'

    # list des fichiers (modifier le path si necessaire)
    dic_pivot_files = {}
    dic_pivot_files['mappings_file'] = path_to_mapping + 'i2b2_mapppings.txt'
    dic_pivot_files['dep_files'] = path_to_scripts + 'map_pivot_dic'
    dic_pivot_files['incre_patient'] = path_to_scripts + 'patient_increment.txt'
    dic_pivot_files['metadata_file'] = path_to_mapping + 'i2b2_OSIRIS_meta.csv'
    dic_pivot_files['patient'] = path_to_data + 'OSIRIS_pivot_Patient.csv'
    dic_pivot_files['visit'] = path_to_data + 'OSIRIS_pivot_TumorPathologyEvent.csv'
    dic_pivot_files['BioSample'] = path_to_data + 'OSIRIS_pivot_BiologicalSample.csv'
    # dic_pivot_files['Analysis'] = path_to_data + 'OSIRIS_pivot_Analysis.csv'
    # dic_pivot_files['BioMarker'] = path_to_data + 'OSIRIS_pivot_Biomarker.csv'
    # dic_pivot_files['Consent'] = path_to_data + 'OSIRIS_pivot_Consent.csv'


    tranfo_data(dic_db_param, dic_pivot_files)


if __name__ == '__main__':
    main()
