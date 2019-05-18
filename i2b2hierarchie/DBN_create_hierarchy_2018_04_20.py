# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 14:36:50 2016

@author: david
"""

import sys, pprint
from DBN_construction_hierarchie_2018_04_20 import constrution_hierarchie
from DBN_construct_metadata_file_20170113 import constuct_metadata_file
from createAdapterMapping import adapter_mapping_builder

#####################
#script de construction d'une hierachie tirée un fichier excel csv txt
#ou freemind en une série de fichier implémentable dans i2b2 et shrine
####################

def lecture_hierachie_file (input_file, proxy_var):
    hierachie = constrution_hierarchie(input_file, 'TEST_OSIRIS', proxy_var,"columnMapping.csv","FileMapping.csv")
    #print type_file
    hierachie.creation_mm_hierarchie()

    return hierachie

### création du fichier de hierarchie i2b2
# le fichier contiendra les lignes de commande sql pour intégrer les données
# dans les tables i2b2metadata.i2b2 et i2b2demodata.concept_dimension

def create_hierachieFileI2b2_csv (hierachie, i2b2_file, config_file):
    i2b2_meta_data = open (i2b2_file + 'meta.txt', 'w')
    i2b2_demo_data = open (i2b2_file + 'demo.txt', 'w')
    i2b2_modif_data = open(i2b2_file + 'modif.txt', 'w')
    i2b2_mappings_data = open(i2b2_file + 'mapppings.txt', 'w')

    action_i2b2meta_sql = constuct_metadata_file(config_file, 'i2b2metadata.i2b2')
    action_i2b2demo_sql = constuct_metadata_file(config_file, 'i2b2demodata.concept_dimension')
    action_i2b2modif_sql = constuct_metadata_file(config_file, 'i2b2demodata.modifier_dimension')

    #i2b2_meta_data.write(action_i2b2meta_sql.add_title_csvfile())
    #i2b2_demo_data.write(action_i2b2demo_sql.add_title_csvfile())
    #i2b2_modif_data.write(action_i2b2modif_sql.add_title_csvfile())

    for id_hierarchie in hierachie.dic_hierarchie:
        #print (hierachie.dic_hierarchie[id_hierarchie])
        i2b2_meta_data.write(action_i2b2meta_sql.add_node_csvfile(hierachie.dic_hierarchie[id_hierarchie]))
        if hierachie.dic_hierarchie[id_hierarchie]['concept_cd'] != '':
            i2b2_demo_data.write(action_i2b2demo_sql.add_node_csvfile(hierachie.dic_hierarchie[id_hierarchie]))
        if hierachie.dic_hierarchie[id_hierarchie]['modifier_cd'] != '':
            i2b2_modif_data.write(action_i2b2modif_sql.add_node_csvfile(hierachie.dic_hierarchie[id_hierarchie]))
            if(hierachie.dic_hierarchie[id_hierarchie]['c_basecode'].startswith('Drug')):
                pprint.pprint(hierachie.dic_hierarchie[id_hierarchie]["c_basecode"])
    # pprint.pprint(hierachie.dic_mappings)
    i2b2_mappings_data.write("concept,column,start_date,end_date,concept_modified\n")
    for i in hierachie.dic_mappings:
        i2b2_mappings_data.write(hierachie.dic_mappings[i]["concept"] + "," + hierachie.dic_mappings[i]["column"] + "," + hierachie.dic_mappings[i]["start_date"] + "," + hierachie.dic_mappings[i]["end_date"] + "," + hierachie.dic_mappings[i]["concept_modified"] + "\n")

    i2b2_meta_data.close()
    i2b2_demo_data.close()
    i2b2_modif_data.close()
    i2b2_mappings_data.close()

### création du fichier de hierarchie  shrine
# le fichier contiendra les lignes de commande sql pour intégrer les données
# dans les tables shrine_ont.shrine
def create_hierachieFileSHRINE_csv (hierachie, shrine_file, config_file):

    shrine_ont = open (shrine_file + '.txt', 'w')
    action_shrine_sql = constuct_metadata_file(config_file, 'shrine_ont.shrine')
    for id_hierarchie in hierachie.dic_hierarchie:
        shrine_ont.writelines(action_shrine_sql.add_node_csvfile(hierachie.dic_hierarchie[id_hierarchie]))
    shrine_ont.close()

### lancement du script
# en input le fichier (txt, csv, xls, xlsx, mm ...) en question
# si c'est un excel, il doit avoir la config suivante ...
# si c'est un csv ou txt (ou equivalant) il faut qu'il soit comme l'exemple
# suivant
# en output les fichiers de hierarchie (csv) correspondant à i2b2 et à Shrine
def main():
    input_file = sys.argv[1]
    config_file = sys.argv[2]
    if sys.argv[3] :
        i2b2_file = sys.argv[3] + 'i2b2_'
        shrine_file = sys.argv[3] + 'shrine_'
    else :
        i2b2_file = 'i2b2_hierachie'
        shrine_file = 'shrine_hierachie'

    proxy_var = {}
    proxy_var['proxy'] = ''
    proxy_var['user'] = ''
    proxy_var['password'] = ''
    proxy_var['url'] = ''
    proxy_var['port'] = ''
    proxy_var['is_proxy'] = False


    hierachie = lecture_hierachie_file (input_file, proxy_var)
    create_hierachieFileI2b2_csv (hierachie, i2b2_file, config_file)
    create_hierachieFileSHRINE_csv (hierachie, shrine_file, config_file)

    # Ajout de adapter mapping
    adapter_builder=adapter_mapping_builder(sys.argv[3]+"shrine_.txt",sys.argv[3]+"AdapterMapping-osiris.csv")
    adapter_builder.lecture_file_i2b2()


if __name__ == '__main__':
    main()
