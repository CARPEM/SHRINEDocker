# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 16:14:46 2016

@author: david
"""
import re, datetime,pprint
from modality_reader import osiris_value_parser
from CreateMappingFiles import mapping_file_builder

#### classe construction hierarchie
# servant à transférer les données contenue dans les différents fichiers pour
# créer le dictionnaire de hierarchie

class constrution_hierarchie:
    # construction de l'objet
    def __init__(self, filename, source, proxy_var, mappingFile, mappingEntityFile):
        self.dic_hierarchie = {}
        self.filename = filename
        self.source = source
        self.dic_order_node = {}
        self.proxy_var = proxy_var
        self.mappingFile = mappingFile
        self.mappingEntityFile = mappingEntityFile
        self.dic_mappings = {}
    # procedure de creation du dictionnaire de donnees a partir d'un fichier
    # freemind

    def creation_mm_hierarchie(self):

        self.dic_hierarchie = {}
        self.dic_order_node = {}
        self.dic_order_node['1'] = 1

        '''
        mm_file = open(self.filename, 'r')
        for line in mm_file: print(line.replace('\n', '').replace('\r', ''))
        mm_file.close()
        '''

        mm_file = open(self.filename, 'r')
        mappingFile = open(self.mappingFile, 'w')
        mappingEntityFile = open(self.mappingEntityFile, 'w')

        mapping_builder = mapping_file_builder(mappingFile, mappingEntityFile)

        indice = 1
        parent_node = []
        parent_node.append('i2b2')
        first_modif_node = ''
        is_first_modif_node_leaf = True
        fullname_M = ''
        list_moda_data = []

        # parent_node.append('racine')
        ind_modif = -1
        is_modif_node = False;
        is_visit_node = False;
        is_patient_node = False
        has_mapping = False
        modif_node = []
        ind_node = indice
        id_node = ""
        name_node = ""
        current_modif_fullname = ""
        current_modif_fullnames = []
        current_modif_fullnames.append("")
        mappings={}

        for line in mm_file:

            line = line.strip()

            balise = self.supprime_accent(line).replace('\n', '').replace('\r', '').split(' ')[0]
            # print(line.replace('\n', '').replace('\r', ''))



            # cas ligne variable
            if balise == '<node':
                if has_mapping:
                    print("add => " + str(mappings))
                    self.dic_mappings[mappings['concept']+"_"+mappings['column']]=mappings
                    mappings ={}
                    has_mapping = False
                id_node = self.recherche_mm_info_node(line, 'ID')
                name_node = self.recherche_mm_info_node(line, 'TEXT')
                ind_node = indice


                if first_modif_node != '': is_first_modif_node_leaf = False

                if line.replace('\n', '').replace('\r', '')[-2] != '/':
                    parent_node.append(name_node)
                    if is_modif_node or is_visit_node or is_patient_node: modif_node.append(name_node)
                    current_modif_fullname = current_modif_fullnames[-1]
                    if current_modif_fullname != "":
                        modif_fullname = current_modif_fullname +name_node + '\\\\'
                    else:
                        modif_fullname = self.take_concept_fullname(modif_node, name_node, True)
                    current_modif_fullname = modif_fullname
                    current_modif_fullnames.append(current_modif_fullname)
                    dic_value = {
                        'name_node': name_node,
                        'parent_node': parent_node[-1],
                        'ind_node': ind_node,
                        'cname': "{0:04}".format(self.dic_order_node['1']) + '_' + name_node,
                        'type_var': 'text',
                        'fullname': self.take_concept_fullname(parent_node, '', False),
                        'modif_fullname': modif_fullname,
                        'type_node': 'FA',
                        'is_leaf': False,
                        'code_concept': id_node,
                        'xml': '',
                        'is_visit': is_visit_node,
                        'is_modif': is_modif_node,
                        'is_patient': is_patient_node,
                        'modif_attrib': 'DA',
                        'ind_modif_node': indice - ind_modif + 1,
                        'fullname_M': fullname_M,
                        'DB': self.source
                    }
                    if is_modif_node:
                        self.add_new_node_in_hierarchieM(id_node, dic_value)
                    elif is_visit_node:
                        self.add_new_node_in_hierarchieV(id_node, dic_value)
                    elif is_patient_node:
                        self.add_new_node_in_hierarchieP(id_node, dic_value)
                    else:
                        self.add_new_node_in_hierarchie(id_node, dic_value)
                    # print("current_modif_fullname 1 ==>")
                    # print(current_modif_fullname)
                    # print(dic_value['modif_fullname'])
                    indice += 1
                    self.dic_order_node['1'] += 1
                    # print("Boucle =============================================")
                    # print("ind_node ==>" + str(ind_node))
                    # print("name_node ==>" + name_node)
                    # print("id_node ==>" + id_node)
                    # pprint.pprint(parent_node)
                    # print("is_modif_node ==>" + str(is_modif_node))
                    # print('fullname ==> ' + self.take_concept_fullname(parent_node, '', False)),
                    # print('modif_fullname ==> ' + self.take_concept_fullname(modif_node, '', False)),
                    # print("fullname_M ==>" + fullname_M)
                    # print("first_modif_node ==>" + str(first_modif_node))
                    # print("is_first_modif_node_leaf ==>" + str(is_first_modif_node_leaf))
                else:
                    dic_value = {
                        'name_node': name_node,
                        'parent_node': parent_node[-1],
                        'ind_node': ind_node,
                        'cname': "{0:04}".format(self.dic_order_node['1']) + '_' + name_node,
                        'type_var': 'text',
                        'fullname': self.take_concept_fullname(parent_node, name_node, True),
                        'modif_fullname': modif_fullname,
                        'type_node': 'LA',
                        'is_leaf': True,
                        'code_concept': '',
                        'xml': '',
                        'is_visit': is_visit_node,
                        'is_modif': is_modif_node,
                        'is_patient': is_patient_node,
                        'modif_attrib': 'RA',
                        'ind_modif_node': indice - ind_modif + 1,
                        'fullname_M': fullname_M,
                        'DB': self.source
                    }
                    if is_modif_node:
                        self.add_new_node_in_hierarchieM(id_node, dic_value)
                    elif is_visit_node:
                        self.add_new_node_in_hierarchieV(id_node, dic_value)
                    elif is_patient_node:
                        self.add_new_node_in_hierarchieP(id_node, dic_value)
                    else:
                        self.add_new_node_in_hierarchie(id_node, dic_value)
                    self.dic_order_node['1'] += 1

                    # print("Boucle 2 =============================================")
                    # print("ind_node ==>" + str(ind_node))
                    # print("name_node ==>" + name_node)
                    # print("id_node ==>" + id_node)
                    # pprint.pprint(parent_node)
                    # print("is_modif_node ==>" + str(is_modif_node))
                    # print('fullname ==> ' + self.take_concept_fullname(parent_node, '', False)),
                    # print('modif_fullname ==> ' + self.take_concept_fullname(modif_node, '', False)),
                    # print("fullname_M ==>" + fullname_M)
                    # print("first_modif_node ==>" + str(first_modif_node))
                    # print("is_first_modif_node_leaf ==>" + str(is_first_modif_node_leaf))
            # cas fin d'embranchement
            elif balise == '</node>':
                indice = indice - 1
                if first_modif_node != '':
                    if is_first_modif_node_leaf:
                        self.dic_hierarchie[first_modif_node]['c_visualattributes'] = 'DA'
                    else:
                        self.dic_hierarchie[first_modif_node]['c_visualattributes'] = 'DA'
                    self.dic_hierarchie[first_modif_node]['chlevel'] = '1'
                    self.dic_hierarchie[first_modif_node]['c_hlevel'] = '1'
                    first_modif_node = ''
                    is_first_modif_node_leaf = True
                if dic_value['ind_node'] != str(ind_node) and is_modif_node:
                    self.dic_hierarchie[id_node]['c_visualattributes'] = 'DA'
                if is_modif_node:
                    del modif_node[-1]
                    del current_modif_fullnames[-1]
                elif is_visit_node:
                    del modif_node[-1]
                elif is_patient_node:
                    del modif_node[-1]
                del parent_node[-1]
                if has_mapping:
                    print("add => " + str(mappings))
                    self.dic_mappings[mappings['concept']+"_"+mappings['column']]=mappings
                    mappings ={}
                    has_mapping = False
            # gestion des indices pour le C_HLEVEL
            # print(str(ind_modif))
            # print(str(indice))
            if ind_modif >= indice:
                is_modif_node = False;
                is_visit_node = False;
                is_patient_node = False
                current_modif_fullname = ""
                fullname_M = ''
                modif_node = []
                ind_modif = -1

            # cas modifier
            if line.replace('\n', '').replace('\r', '') == '<icon BUILTIN="messagebox_warning"/>' and not is_modif_node:
                ind_modif = ind_node
                modif_node.append(name_node)
                first_modif_node = id_node

                del self.dic_hierarchie[id_node]
                dic_value['parent_node'] = parent_node[-1]
                dic_value['fullname'] = self.take_concept_fullname(parent_node[:-1], name_node, False)
                fullname_M = dic_value['fullname']
                dic_value['fullname_M'] = fullname_M
                # print(self.take_concept_fullname(modif_node, name_node, False))
                # print(modif_node)
                dic_value['modif_fullname'] = "\\\\"+parent_node[-2]+self.take_concept_fullname(modif_node, name_node, dic_value['is_leaf'])
                # print(parent_node)
                current_modif_fullnames.append(dic_value['modif_fullname'])
                # print("current_modif_fullname ==> " + str(current_modif_fullnames))
                self.add_new_node_in_hierarchieM(id_node, dic_value)
                is_modif_node = True

            # cas modalites
            if line.replace('\n', '').replace('\r', '')[:26] == '<attribute NAME="modality"':

                self.dic_hierarchie[id_node]['c_visualattributes'] = 'FA'
                dic_parent_node = dic_value
                url = self.recherche_mm_info_node(line, 'VALUE')
                list_moda_data = []
                # print(url)

                #TODO Remplacer le parser pour lire le TSV
                modality_parser = osiris_value_parser(url)
                # if self.proxy_var['is_proxy']:
                #     # print('add proxy')
                #     modality_parser.add_proxy(self.proxy_var['user'], self.proxy_var['password'], self.proxy_var['url'])
                #     # print('launch parsing')
                #     modality_data = modality_parser.parseWithProxy()
                # else:
                #     modality_data = modality_parser.parse()
                modality_data=modality_parser.parseFromCsv()
                print(modality_data)
                list_moda_data = set([])

                #TODO Attention à la structure de l'objet renvoyé par le parser
                for dic_modility in modality_data:
                    dic_value = dic_parent_node
                    dic_value['id_node'] = dic_modility['code']
                    dic_value['cname'] = dic_modility['code'] +"-"+ dic_modility['Label']
                    dic_value['type_node'] = 'LA'
                    if is_modif_node:
                        dic_value['ind_modif_node'] = indice - ind_modif + 2
                        dic_value['modif_attrib'] = 'RA'
                        # print(dic_value['parent_node'])
                        # print(dic_value['cname'])
                        self.add_new_modalite_in_hierarchieM(
                            str(id_node) + dic_value['parent_node'] + '|' + dic_value['cname'], dic_value)
                    else:
                        self.add_new_modalite_in_hierarchie(
                            str(id_node) + dic_value['parent_node'] + '|' + dic_value['cname'], dic_value)
                    list_moda_data.add(str(id_node) + dic_value['parent_node'] + '|' + dic_value['cname'])

            if line.replace('\n', '').replace('\r', '')[:25] == '<attribute NAME="concept"':
                concept = self.recherche_mm_info_node(line, 'VALUE')

                mapping_builder.addToEntiy(concept)

                #id_moda = str(id_node) + dic_value['parent_node'] + '|' + dic_value['id_node']
                for moda_data in list_moda_data:
                    self.dic_hierarchie[moda_data]['c_basecode'] = concept + '|' + self.dic_hierarchie[moda_data][
                        'c_basecode']
                    self.dic_hierarchie[moda_data]['concept_cd'] = concept + '|' + self.dic_hierarchie[moda_data][
                        'concept_cd']
                if len(list_moda_data) == 0 :
                    if concept == dic_value['name_node']:
                        self.dic_hierarchie[id_node]['c_basecode'] = concept
                        self.dic_hierarchie[id_node]['concept_cd'] = concept
                    else:
                        mapping_builder.addToModa(concept,dic_value['name_node'],'0')
                        self.dic_hierarchie[id_node]['c_basecode'] = concept + '|' + dic_value[
                            'name_node']
                        self.dic_hierarchie[id_node]['concept_cd'] = concept + '|' + dic_value[
                            'name_node']
                else:
                    mapping_builder.addToModa(concept,dic_value['name_node'],'1')
                list_moda_data = []
                if has_mapping:
                    mappings["concept"]=concept
            if line.replace('\n', '').replace('\r', '')[:28] == '<attribute NAME="start_date"':
                start_date = self.recherche_mm_info_node(line, 'VALUE')
                if not has_mapping:
                    mappings=self.create_mapping(name_node,concept)
                    has_mapping = True
                mappings["start_date"]=start_date
                print(mappings)
            if line.replace('\n', '').replace('\r', '')[:26] == '<attribute NAME="end_date"':
                end_date = self.recherche_mm_info_node(line, 'VALUE')
                if not has_mapping:
                    mappings=self.create_mapping(name_node,concept)
                    has_mapping = True
                mappings["end_date"]=end_date
                print(mappings)
            if line.replace('\n', '').replace('\r', '')[:28] == '<attribute NAME="c_modified"':
                    concept_modified = self.recherche_mm_info_node(line, 'VALUE')
                    if not has_mapping:
                        mappings=self.create_mapping(name_node,concept)
                        has_mapping = True
                    mappings["concept_modified"]=concept_modified
                    print(mappings)
            '''
            # cas patient

            elif line.replace('\n', '').replace('\r', '') == '<icon BUILTIN="male1"/>' and not is_patient_node:
                print(dic_value)
                ind_modif = ind_node
                modif_node.append(name_node)

                del self.dic_hierarchie[id_node]
                dic_value['parent_node'] = parent_node[-1]
                dic_value['fullname'] = self.take_concept_fullname(parent_node[:-1], name_node, False)
                dic_value['modif_fullname'] = self.take_concept_fullname(modif_node, name_node, dic_value['is_leaf'])
                self.add_new_node_in_hierarchieP(id_node, dic_value)
                is_patient_node = True

            # cas visit
            elif line.replace('\n', '').replace('\r', '') == '<icon BUILTIN="bookmark"/>' and not is_visit_node:
                print(dic_value)
                ind_modif = ind_node
                modif_node.append(name_node)

                del self.dic_hierarchie[id_node]
                dic_value['parent_node'] = parent_node[-1]
                dic_value['fullname'] = self.take_concept_fullname(parent_node[:-1], name_node, False)
                dic_value['modif_fullname'] = self.take_concept_fullname(modif_node, name_node, dic_value['is_leaf'])
                self.add_new_node_in_hierarchieV(id_node, dic_value)
                is_visit_node = True
                '''

            # cas variable numerique
            if line.replace('\n', '').replace('\r', '') == '<icon BUILTIN="full-1"/>':
                self.dic_hierarchie[id_node]['type_var'] = 'numeric'
                self.dic_hierarchie[id_node]['c_metadataxml'] = 'xml'
                self.dic_hierarchie[id_node]['c_columndatatype'] = 'N'

        # pprint.pprint(self.dic_hierarchie)
        mapping_builder.writeMappings()
        mappingFile.close()
        mappingEntityFile.close()
    # fonction servant a rechercher dans une chaine de caracetere issu d'un
    # fichier freemind la valeur recherhcher

    def create_mapping(self,name_node,concept):
        if name_node ==concept:
            name_node="Instance_Id"
        return {
            "concept": concept,
            "column": name_node,
            "start_date": "",
            "end_date": "",
            "concept_modified": ""
        }
    def recherche_mm_info_node(self, cible, text):
        match_info = re.search(text + '=\".*\"', cible)
        if match_info:
            res = match_info.group(0).split('\"')
            return res[1]
        return ''

    def take_concept_fullname(self, parent_node, name_node, name_node_given):
        if parent_node == []: return ''
        res = '\\\\'
        for node in parent_node:
            res += node + '\\\\'
        if name_node_given:
            if name_node != '':
                res += name_node + '\\\\'
            else:
                res += 'warning_not_name_node\\\\'
        return res

    def add_new_node_in_hierarchie(self, id_node, dic_value):
        self.dic_hierarchie[id_node] = {
            'chlevel': str(dic_value['ind_node']),
            'c_hlevel': str(dic_value['ind_node']),
            'c_fullname': str(dic_value['fullname']),
            'c_name': str(dic_value['cname']),
            'c_synonym_cd': 'N',
            'c_visualattributes': str(dic_value['type_node']),
            'c_basecode': str(id_node),
            'c_metadataxml': str(dic_value['xml']),
            'c_facttablecolumn': 'concept_cd',
            'c_tablename': 'concept_dimension',
            'c_columnname': 'concept_path',
            'c_columndatatype': 'T',
            'c_operator': 'LIKE',
            'c_dimcode': str(dic_value['fullname']),
            'c_tooltip': str(dic_value['fullname']),
            'm_applied_path': '@',
            'update_date': str(datetime.datetime.now()),
            'download_date': str(datetime.datetime.now()),
            'import_date': str(datetime.datetime.now()),
            'sourcesystem_cd': str(dic_value['DB']),
            'concept_path': str(dic_value['fullname']),
            'concept_cd': str(id_node),
            'name_char': str(dic_value['name_node']),
            'modifier_path': '',
            'modifier_cd': '',
            'modifier_blob': '',
            'concept_blob': '',
            'upload_id': 'None',
            'c_totalnum': 'None',
            'c_comment': 'None',
            'valuetype_cd': 'None',
            'm_exclusion_cd': 'None',
            'c_path': 'None',
            'c_symbol': 'None'
        }

    def add_new_modalite_in_hierarchie(self, id_node, dic_value):
        c_fullname = str(dic_value['fullname'] + self.supprime_accent(dic_value['cname'].replace(' ',''))+ '\\\\')
        self.dic_hierarchie[id_node] = {
            'chlevel': str(dic_value['ind_modif_node'] -1),
            'c_hlevel': str(dic_value['ind_modif_node'] -1),
            'c_fullname': c_fullname,
            'c_name': str(dic_value['cname']),
            'c_synonym_cd': 'N',
            'c_visualattributes': str(dic_value['type_node']),
            'c_basecode': str(dic_value['parent_node'] + '|' + dic_value['id_node']),
            'c_metadataxml': str(dic_value['xml']),
            'c_facttablecolumn': 'concept_cd',
            'c_tablename': 'concept_dimension',
            'c_columnname': 'concept_path',
            'c_columndatatype': 'T',
            'c_operator': 'LIKE',
            'c_dimcode': c_fullname,
            'c_tooltip': c_fullname,
            'm_applied_path': '@',
            'update_date': str(datetime.datetime.now()),
            'download_date': str(datetime.datetime.now()),
            'import_date': str(datetime.datetime.now()),
            'sourcesystem_cd': str(dic_value['DB']),
            'concept_path': c_fullname,
            'concept_cd': dic_value['parent_node'] + ':' + dic_value['cname'],
            'name_char': str(dic_value['name_node']),
            'modifier_path': '',
            'modifier_cd': '',
            'modifier_blob': '',
            'concept_blob': '',
            'upload_id': 'None',
            'c_totalnum': 'None',
            'c_comment': 'None',
            'valuetype_cd': 'None',
            'm_exclusion_cd': 'None',
            'c_path': 'None',
            'c_symbol': 'None'
        }


    def add_new_node_in_hierarchieM(self, id_node, dic_value):
        self.dic_hierarchie[id_node] = {
            'chlevel': str(dic_value['ind_modif_node']),
            'c_hlevel': str(dic_value['ind_modif_node']),
            'c_fullname': str(dic_value['modif_fullname']),
            'c_name': str(dic_value['cname']),
            'c_synonym_cd': 'N',
            'c_visualattributes': dic_value['modif_attrib'],
            'c_basecode': str(id_node),
            'c_metadataxml': str(dic_value['xml']),
            'c_facttablecolumn': 'MODIFIER_CD',
            'c_tablename': 'MODIFIER_DIMENSION',
            'c_columnname': 'MODIFIER_PATH',
            'c_columndatatype': 'T',
            'c_operator': 'LIKE',
            'c_dimcode': str(dic_value['modif_fullname']),
            'c_tooltip': str(dic_value['modif_fullname']),
            'm_applied_path': str(dic_value['fullname_M'] + '%'),
            'update_date': str(datetime.datetime.now()),
            'download_date': str(datetime.datetime.now()),
            'import_date': str(datetime.datetime.now()),
            'sourcesystem_cd': str(dic_value['DB']),
            'concept_path': '',
            'concept_cd': '',
            'name_char': str(dic_value['name_node']),
            'modifier_path': str(dic_value['modif_fullname']),
            'modifier_cd': str(id_node),
            'modifier_blob': '',
            'concept_blob': '',
            'upload_id': 'None',
            'c_totalnum': 'None',
            'c_comment': 'None',
            'valuetype_cd': 'None',
            'm_exclusion_cd': 'None',
            'c_path': 'None',
            'c_symbol': 'None'
        }
        # print("==================================")
        # print(self.dic_hierarchie[id_node]["c_name"])
        # print(self.dic_hierarchie[id_node]["c_fullname"])
        # print(self.dic_hierarchie[id_node]["c_hlevel"])

    def add_new_modalite_in_hierarchieM(self, id_node, dic_value):
        c_fullname = str(dic_value['modif_fullname'] + self.supprime_accent(dic_value['cname'].replace(' ','_'))+ '\\\\')
        # pprint.pprint(dic_value)
        # print(str(dic_value['parent_node'] + '|' + dic_value['id_node']))
        self.dic_hierarchie[id_node] = {
            'chlevel': str(dic_value['ind_modif_node']-1),
            'c_hlevel': str(dic_value['ind_modif_node']-1),
            'c_fullname': c_fullname,
            'c_name': str(dic_value['cname']),
            'c_synonym_cd': 'N',
            'c_visualattributes': dic_value['modif_attrib'],
            'c_basecode': str(dic_value['parent_node'] + '|' + dic_value['id_node']),
            'c_metadataxml': str(dic_value['xml']),
            'c_facttablecolumn': 'MODIFIER_CD',
            'c_tablename': 'MODIFIER_DIMENSION',
            'c_columnname': 'MODIFIER_PATH',
            'c_columndatatype': 'T',
            'c_operator': 'LIKE',
            'c_dimcode': c_fullname,
            'c_tooltip': c_fullname,
            'm_applied_path': str(dic_value['fullname_M'] + '%'),
            'update_date': str(datetime.datetime.now()),
            'download_date': str(datetime.datetime.now()),
            'import_date': str(datetime.datetime.now()),
            'sourcesystem_cd': str(dic_value['DB']),
            'concept_path': '',
            'concept_cd': '',
            'name_char': str(dic_value['name_node']),
            'modifier_path': c_fullname,
            'modifier_cd': dic_value['parent_node'] + ':' + dic_value['cname'],
            'modifier_blob': '',
            'concept_blob': '',
            'upload_id': 'None',
            'c_totalnum': 'None',
            'c_comment': 'None',
            'valuetype_cd': 'None',
            'm_exclusion_cd': 'None',
            'c_path': 'None',
            'c_symbol': 'None'
        }
        # pprint.pprint(self.dic_hierarchie[id_node])

    def add_new_node_in_hierarchieP(self, id_node, dic_value):
        self.dic_hierarchie[id_node] = {
            'chlevel': '1',
            'c_hlevel': '1',
            'c_fullname': str(dic_value['modif_fullname']),
            'c_name': str(dic_value['cname']),
            'c_synonym_cd': 'N',
            'c_visualattributes': 'RA',
            'c_basecode': str(id_node),
            'c_metadataxml': str(dic_value['xml']),
            'c_facttablecolumn': 'patient_num',
            'c_tablename': 'patient_dimension',
            'c_columnname': str(dic_value['name_node']),
            'c_columndatatype': 'T',
            'c_operator': 'LIKE',
            'c_dimcode': str(dic_value['modif_fullname']),
            'c_tooltip': str(dic_value['modif_fullname']),
            'm_applied_path': str(dic_value['fullname']),
            'update_date': str(datetime.datetime.now()),
            'download_date': str(datetime.datetime.now()),
            'import_date': str(datetime.datetime.now()),
            'sourcesystem_cd': str(dic_value['DB']),
            'concept_path': '',
            'concept_cd': '',
            'name_char': str(dic_value['name_node']),
            'modifier_path': str(dic_value['modif_fullname']),
            'modifier_cd': str(id_node),
            'modifier_blob': '',
            'concept_blob': '',
            'upload_id': 'None',
            'c_totalnum': 'None',
            'c_comment': 'None',
            'valuetype_cd': 'None',
            'm_exclusion_cd': 'None',
            'c_path': 'None',
            'c_symbol': 'None'
        }

    def add_new_node_in_hierarchieV(self, id_node, dic_value):
        self.dic_hierarchie[id_node] = {
            'chlevel': '1',
            'c_hlevel': '1',
            'c_fullname': str(dic_value['modif_fullname']),
            'c_name': str(dic_value['cname']),
            'c_synonym_cd': 'N',
            'c_visualattributes': 'RA',
            'c_basecode': str(id_node),
            'c_metadataxml': str(dic_value['xml']),
            'c_facttablecolumn': 'encounter_num',
            'c_tablename': 'visit_dimension',
            'c_columnname': str(dic_value['name_node']),
            'c_columndatatype': 'T',
            'c_operator': 'LIKE',
            'c_dimcode': str(dic_value['modif_fullname']),
            'c_tooltip': str(dic_value['modif_fullname']),
            'm_applied_path': str(dic_value['fullname']),
            'update_date': str(datetime.datetime.now()),
            'download_date': str(datetime.datetime.now()),
            'import_date': str(datetime.datetime.now()),
            'sourcesystem_cd': str(dic_value['DB']),
            'concept_path': '',
            'concept_cd': '',
            'name_char': str(dic_value['name_node']),
            'modifier_path': str(dic_value['modif_fullname']),
            'modifier_cd': str(id_node),
            'modifier_blob': '',
            'concept_blob': '',
            'upload_id': 'None',
            'c_totalnum': 'None',
            'c_comment': 'None',
            'valuetype_cd': 'None',
            'm_exclusion_cd': 'None',
            'c_path': 'None',
            'c_symbol': 'None'
        }

    # fonctions annexe
    def supprime_accent(self, ligne):
        """ supprime les accents de la ligne et aussi d'autre caractere indesirable dans la base de donnees """
        accent = ['é', 'è', 'ê', 'ë', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â', '(', ')', 'Î', 'œ', 'ü', 'ï',
                  'È', 'É', 'Ê', '[', ']']
        sans_accent = ['e', 'e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a', '', '', 'I', 'oe', 'u', 'i',
                       'E', 'E', 'E', '', '']
        caract = "'"
        ligne = ligne.replace(caract, " ")
        ligne = ligne.replace('\n', '')
        i = 0
        for i in range(0, len(accent)):
            ligne = ligne.replace(accent[i], sans_accent[i])
        return ligne
