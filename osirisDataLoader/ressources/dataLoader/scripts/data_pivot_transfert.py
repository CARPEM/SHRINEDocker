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
from script_pivot_transfert.mapping import mapping_osiris
from script_pivot_transfert.request import SQL_request


def search_basecode (var, list_ref):
    i=0
    #if var == 'T': print('recherche de la vaiable TNM_T')
    for ref in list_ref['var_pivot'] :
        #if var == 'T': print(ref)
        if var == ref[len(re.match('.*_', ref).group(0)):]:
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

    # add all file in pivot_files (all file who is reading is indicating in ref_files)
    '''
    dic_files = {}
    for ref_file_key in dic_ref_files['filename']:
        add_file = lecture_csv_file('map_data/' + ref_file_key, ',')
        test_file_found = True
        try:
            dic_files[ref_file_key] = add_file.copy_csv_file()
        except:
            print(ref_file_key + ' not found')
            test_file_found = False
        if test_file_found :
            try:
                pivot.add_file_into_data(dic_files[ref_file_key], ref_file_key)
            except:
                print(pivot.error_message)
    '''
    return pivot


def load_i2b2_metadata(dic_db_param, sql_file):
    dic_i2b2_metadata = {}
    dic_i2b2_metadata['var_i2b2'] = []
    dic_i2b2_metadata['table_i2b2'] = []
    dic_i2b2_metadata['type_var_i2b2'] = []
    dic_i2b2_metadata['var_pivot'] = []
    dic_i2b2_metadata['basecode_i2b2'] = []

    # create a connexion between i2b2 database
    interac_i2b2 = i2b2_interaction(dic_db_param['DB_type'], dic_db_param['DB_host'], dic_db_param['DB_name'],
                                    dic_db_param['DB_port'], dic_db_param['BD_user'], dic_db_param['DB_password'])

    # execute select metadata request
    sql_take_i2b2_metadata = open(dic_db_param['path_to_scripts'] + sql_file, 'r')
    tab_metadata = interac_i2b2.executeBasicRequest_n(sql_take_i2b2_metadata.read(), 4)

    # transfert result to tab_metadata
    for metadata in tab_metadata:
        dic_i2b2_metadata['var_i2b2'].append(metadata[0][len(re.match('.*_', metadata[0]).group(0)):])
        dic_i2b2_metadata['var_pivot'].append(metadata[0])
        dic_i2b2_metadata['table_i2b2'].append(metadata[1])
        dic_i2b2_metadata['type_var_i2b2'].append(metadata[2])
        dic_i2b2_metadata['basecode_i2b2'].append(metadata[3])
    return dic_i2b2_metadata


def lect_i2b2_metadata(metadata_file, conmod_id):
    meta_file = lecture_csv_file(metadata_file, ',')
    dic_meta = meta_file.copy_csv_file()
    i = 0

    # preparation du dic de meta i2b2
    dic_i2b2_metadata = {}
    dic_i2b2_metadata['var_i2b2'] = []
    dic_i2b2_metadata['table_i2b2'] = []
    dic_i2b2_metadata['type_var_i2b2'] = []
    dic_i2b2_metadata['var_pivot'] = []
    dic_i2b2_metadata['basecode_i2b2'] = []
    dic_i2b2_metadata['ref_concept'] = []

    # tval_char = [x for x in dic_meta['tval_char'] if x not in ('', 'E')]
    for metadata in dic_meta['tval_char']:
        if metadata not in ('', 'E', '@'):
            if dic_meta['modifier_cd'][i] not in ('', '@'):
                dic_i2b2_metadata['var_i2b2'].append(metadata)
                dic_i2b2_metadata['var_pivot'].append(metadata)
                dic_i2b2_metadata['table_i2b2'].append('modifier_dimension')
                dic_i2b2_metadata['ref_concept'].append(search_basecode(dic_meta['concept_cd'][i], conmod_id))
                dic_i2b2_metadata['type_var_i2b2'].append('T')
                dic_i2b2_metadata['basecode_i2b2'].append(search_basecode(metadata[len(re.match('.*_', metadata).group(0)):], conmod_id))
            else:
                dic_i2b2_metadata['var_i2b2'].append(metadata)
                dic_i2b2_metadata['var_pivot'].append(metadata)
                dic_i2b2_metadata['table_i2b2'].append('concept_dimension')
                dic_i2b2_metadata['ref_concept'].append(search_basecode(dic_meta['concept_cd'][i][len(re.match('.*_', dic_meta['concept_cd'][i]).group(0)):], conmod_id))
                dic_i2b2_metadata['type_var_i2b2'].append('T')
                dic_i2b2_metadata['basecode_i2b2'].append(search_basecode(metadata[len(re.match('.*_', dic_meta['tval_char'][i]).group(0)):], conmod_id))
        i += 1

    for metadata in dic_meta['nval_num']:
        if metadata != '':
            if dic_meta['modifier_cd'][i] not in ('', '@'):
                dic_i2b2_metadata['var_i2b2'].append(metadata)
                dic_i2b2_metadata['var_pivot'].append(metadata)
                dic_i2b2_metadata['table_i2b2'].append('modifier_dimension')
                dic_i2b2_metadata['ref_concept'].append(search_basecode(dic_meta['concept_cd'][i][len(re.match('.*_', dic_meta['concept_cd'][i]).group(0)):], conmod_id))
                dic_i2b2_metadata['type_var_i2b2'].append('N')
                dic_i2b2_metadata['basecode_i2b2'].append(
                    search_basecode(metadata[len(re.match('.*_', metadata).group(0)):], conmod_id))
            else:
                dic_i2b2_metadata['var_i2b2'].append(metadata)
                dic_i2b2_metadata['var_pivot'].append(metadata)
                dic_i2b2_metadata['table_i2b2'].append('concept_dimension')
                dic_i2b2_metadata['ref_concept'].append(search_basecode(dic_meta['concept_cd'][i][len(re.match('.*_', dic_meta['concept_cd'][i]).group(0)):], conmod_id))
                dic_i2b2_metadata['type_var_i2b2'].append('N')
                dic_i2b2_metadata['basecode_i2b2'].append(search_basecode(metadata[len(re.match('.*_', dic_meta['tval_char'][i]).group(0)):], conmod_id))
        i += 1
    return dic_i2b2_metadata


def match_i2b2_metadata_with_dic_pivot(pivot, patvis_to_transfert, conmod_to_transfert, outputfile, logfile,
                                       dic_db_param):
    i = 0
    f_output = open(outputfile, 'w')
    #pprint.pprint(pivot.dicData)

    req = SQL_request()
    interac_i2b2 = i2b2_interaction(dic_db_param['DB_type'], dic_db_param['DB_host'], dic_db_param['DB_name'],
                                    dic_db_param['DB_port'], dic_db_param['BD_user'], dic_db_param['DB_password'])

    # cas patient et visit
    obj_mapping = mapping_osiris(pivot, patvis_to_transfert, dic_db_param['source'])
    for metadata in patvis_to_transfert['var_i2b2']:

        i2b2_var = metadata
        i2b2_table_cible = patvis_to_transfert['table_i2b2'][i]
        i2b2_type = patvis_to_transfert['type_var_i2b2'][i]
        i2b2_concept_ref = patvis_to_transfert['basecode_i2b2'][i]
        # search data info from metadata
        link_map_data = obj_mapping.find_refvar_in_pivot(i2b2_var)

        # pprint.pprint(i2b2_var)
        # pprint.pprint(i2b2_table_cible)
        # pprint.pprint(i2b2_type)

        if link_map_data != None:
            for patient in pivot.list_key_ref[link_map_data]['listPatient']:

                # select all data needed
                if i2b2_table_cible == 'patient_dimension':
                    dic_data_spe = obj_mapping.transfert_patient_from_pivot(i2b2_var, patient, i2b2_concept_ref)
                    # build insert request
                    if dic_data_spe['tvalue'] != None or dic_data_spe['nvalue'] != None : interac_i2b2.insert_data(req.write_insert_i2b2_data(dic_data_spe), obj_mapping.listvar)
                    # copy resquest to outputfile
                    # f_output.writelines(req.write_insert_i2b2_data(dic_data_spe))

                if i2b2_table_cible == 'visit_dimension':
                    #print(metadata)
                    for visit in pivot.list_key_ref[link_map_data]['listPatient'][patient]:
                        dic_data_spe = obj_mapping.transfert_visit_from_pivot(i2b2_var, patient, visit, i2b2_concept_ref)
                        # build insert request
                        if dic_data_spe['tvalue'] != None or dic_data_spe['nvalue'] != None: interac_i2b2.insert_data(req.write_insert_i2b2_data(dic_data_spe), obj_mapping.listvar)
                        dic_data_spe['table'] = 'visit_dimension'
                        interac_i2b2.insert_data(req.write_insert_i2b2_data(dic_data_spe), [dic_data_spe['tvalue'], dic_data_spe['patient_num'], dic_data_spe['visit_num']])
                        # copy resquest to outputfile
                        # f_output.writelines(req.write_insert_i2b2_data(dic_data_spe))


        i += 1

    # cas concept et modifier
    '''
    obj_mapping = mapping_osiris(pivot, conmod_to_transfert)
    i = 0

    for metadata in conmod_to_transfert['var_i2b2']:
        i2b2_var = metadata
        i2b2_table_cible = conmod_to_transfert['table_i2b2'][i]
        i2b2_type = conmod_to_transfert['type_var_i2b2'][i]
        i2b2_concept_ref = conmod_to_transfert['ref_concept'][i]
        i2b2_basecode = conmod_to_transfert['basecode_i2b2'][i]
        # search data info from metadata
        link_map_data = obj_mapping.find_refvar_in_pivot(i2b2_var)
        if link_map_data != None:
            for patient in pivot.list_key_ref[link_map_data]['listPatient']:

                if i2b2_table_cible == 'concept_dimension':
                    print('codage en cours occurence ' + str(i) + ' nom de la variable ref : ' + link_map_data)
                    for instance in pivot.list_key_ref[link_map_data]['listPatient'][patient]:
                        dic_data_spe = obj_mapping.transfert_concept_from_pivot(i2b2_var, patient, instance, i2b2_type, i2b2_basecode)
                        # copy resquest to outputfile
                        f_output.writelines(req.write_obsdata_csv_file(dic_data_spe))
                        # transfert des donnees suivant le patient_num, le tpe, la var/value,

                if i2b2_table_cible == 'modifier_dimension':
                    print('codage en cours occurence ' + str(i) + ' nom de la variable ref : ' + link_map_data)
                    for instance in pivot.list_key_ref[link_map_data]['listPatient'][patient]:
                        dic_data_spe = obj_mapping.transfert_modifier_from_pivot(i2b2_var, patient, instance, i2b2_type, i2b2_basecode, i2b2_concept_ref)
                        # copy resquest to outputfile
                        pprint.pprint(dic_data_spe)
                        f_output.writelines(req.write_obsdata_csv_file(dic_data_spe))
        i += 1

    '''
    f_output.close()


def tranfo_data(dic_db_param, dic_pivot_files):
    # create json file
    pivot = download_pivot_file(dic_db_param, dic_pivot_files)
    # pprint.pprint(pivot.dicData)
    # print(pivot.dicData['L304']['TumorPathologyEvent_Ref']['2']['BiologicalSample_Ref'])
    # pprint.pprint(pivot.list_key_ref['Analysis_Ref']['listPatient'])
    # pprint.pprint(pivot.list_key_ref['TumorPathologyEvent_Ref']['listPatient'])

    # import i2b2 metadata file
    patvis_to_transfert = load_i2b2_metadata(dic_db_param, dic_db_param['patvis_sql'])
    conmod_id = load_i2b2_metadata(dic_db_param, dic_db_param['conceptmodif_sql'])
    conmod_to_transfert = lect_i2b2_metadata(dic_pivot_files['metadata_file'], conmod_id)

    # pprint.pprint(metadata_to_transfert)

    # map i2b2 metadata to json file
    match_i2b2_metadata_with_dic_pivot(pivot, patvis_to_transfert, conmod_to_transfert, dic_db_param['output_file'],
                                       dic_db_param['log_file'], dic_db_param)

    # print(metadata_to_transfert)


def main():

    path_to_scripts='/opt/dataLoader/scripts/'
    path_to_data='/opt/data_to_load/'

    # DB parameters
    dic_db_param = {}
    dic_db_param['DB_host'] = os.environ['I2B2_DB_HOST']
    dic_db_param['DB_name'] = os.environ['POSTGRES_DB']
    dic_db_param['DB_port'] = os.environ['I2B2_DB_PORT']
    dic_db_param['BD_user'] =  os.environ['POSTGRES_USER']
    dic_db_param['DB_password'] = os.environ['POSTGRES_PASSWORD']
    dic_db_param['DB_type'] = os.environ['SERVER_TYPE']
    dic_db_param['path_to_scripts'] = path_to_scripts
    dic_db_param['patvis_sql'] = 'select_i2b2_metadata.sql'
    dic_db_param['conceptmodif_sql'] = 'select_concept_modif_id.sql'
    dic_db_param['output_file'] = 'osiris_test_logfile.csv'
    dic_db_param['log_file'] = 'osiris_test_output.csv'
    dic_db_param['source'] = 'TEST_OSIRIS'




    # DB parameters
    # dic_db_param = {}
    # dic_db_param['DB_host'] = 'i2b2'
    # dic_db_param['DB_name'] = 'i2b2'
    # dic_db_param['DB_port'] = '5432'
    # dic_db_param['BD_user'] = 'postgres'
    # dic_db_param['DB_password'] = ''
    # dic_db_param['DB_type'] = 'postgresql'
    # dic_db_param['path_to_scripts'] = path_to_scripts
    # dic_db_param['patvis_sql'] = 'select_i2b2_metadata.sql'
    # dic_db_param['conceptmodif_sql'] = 'select_concept_modif_id.sql'
    # dic_db_param['output_file'] = 'osiris_test_logfile.csv'
    # dic_db_param['log_file'] = 'osiris_test_output.csv'
    # dic_db_param['source'] = 'TEST_OSIRIS'




    # list des fichiers (modifier le path si necessaire)
    dic_pivot_files = {}
    dic_pivot_files['dep_files'] = path_to_scripts + 'map_pivot_dic'
    dic_pivot_files['incre_patient'] = path_to_scripts + 'patient_increment.txt'
    dic_pivot_files['metadata_file'] = path_to_data + 'i2b2_OSIRIS_meta.csv'
    dic_pivot_files['patient'] = path_to_data + 'OSIRIS_pivot_Patient.csv'
    dic_pivot_files['visit'] = path_to_data + 'OSIRIS_pivot_TumorPathologyEvent.csv'
    dic_pivot_files['BioSample'] = path_to_data + 'OSIRIS_pivot_BiologicalSample.csv'
    dic_pivot_files['Analysis'] = path_to_data + 'OSIRIS_pivot_Analysis.csv'
    dic_pivot_files['BioMarker'] = path_to_data + 'OSIRIS_pivot_Biomarker.csv'
    dic_pivot_files['Consent'] = path_to_data + 'OSIRIS_pivot_Consent.csv'

    tranfo_data(dic_db_param, dic_pivot_files)


if __name__ == '__main__':
    main()
