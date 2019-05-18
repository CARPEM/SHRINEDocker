# -*- coding: utf-8 -*-
"""
Created 2018/01/03

@author: David BAUDOIN

fonction : script lisant les fichier csv ou de type csv et renvoyant un dictionnaire le contenu sous la forme :
    Dic_var[var1]=[data11, data12, ...]
    Dic_var[var2]=[data21, data22, ...]
    ...
"""
import csv

class lecture_csv_file:

    # construction de l'objet
    def __init__(self, filename, separator):
        self.filename = filename
        self.dic_data = {}
        self.separator = separator

    # action permmetant de retourner les valeurs
    def copy_csv_file(self):
        f_csv = open (self.filename, 'r')

        #titles = f_csv.readline().replace('\n', '').lower().split(self.separator)
        titles = f_csv.readline().replace('\n', '').split(self.separator)
        for title in titles :
            self.dic_data[title] = []
        #print (titles)
        j = 0
        for line in f_csv :
            i = 0
            liste = line.replace('\n', '').split(self.separator)
            if len(titles) != len(liste):
                print('warning a la ligne ' + str(j) + ' manque de donnees possible')
                print(liste)
            else:
                for value in liste:
                    self.dic_data[titles[i]].append(value)
                    i+=1
            j+=1
        return self.dic_data

        # action permmetant de retourner les valeurs

    def copy_csv_file_2col(self):
        ## fonction sortant les resultats sous la forme :
        ## Dic_var[data11]=data12
        ## Dic_var[data21]=data22
        ## ...
        f_csv = open (self.filename, 'r')

        for line in f_csv:
            liste = line.replace('\n', '').split(self.separator)
            self.dic_data[liste[0]] = liste[1]
        return self.dic_data

    def copy_csv_to_dict_tuple_index(self):
        '''
        Fonction retournant un dict sous forme :
        {(concept,column): {'start_date': {value},'end_date': {value},'concept_modified': {value}}

        To get end date value : my_dict['TumorPathologyEvent','Type']['end_date']

        :return: dico :
        {('Drug', 'Code'): {'concept_modified': 'Treatment','end_date': '','start_date': ''},
        ('Patient', 'LastNewsStatus'): {'concept_modified': '','end_date': '','start_date': 'LastNewsDate'},
        ('TNM', 'M'): {'concept_modified': 'TNM', 'end_date': '', 'start_date': ''},
        ('TNM', 'N'): {'concept_modified': 'TNM', 'end_date': '', 'start_date': ''},
        ('TNM', 'T'): {'concept_modified': 'TNM', 'end_date': '', 'start_date': ''},
        ('TNM', 'TNMType'): {'concept_modified': 'TNM','end_date': '','start_date': ''},
        ('TNM', 'TNMVersion'): {'concept_modified': 'TNM','end_date': '','start_date': ''},
        ('TumorPathologyEvent', 'Laterality'): {'concept_modified': '','end_date': 'EndDate','start_date': 'StartDate'},
        ('TumorPathologyEvent', 'MorphologyCode'): {'concept_modified': '','end_date': 'EndDate','start_date': 'StartDate'},
        ('TumorPathologyEvent', 'TopographyCode'): {'concept_modified': '','end_date': 'EndDate','start_date': 'StartDate'},
        ('TumorPathologyEvent', 'Type'): {'concept_modified': '','end_date': 'EndDate','start_date': 'StartDate'}}

        '''
        self.my_dict = {}
        with open(self.filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            start_date = 'start_date'
            end_date = 'end_date'
            concept_modified = 'concept_modified'

            # parsing and creating a row in my_dict for each row in mapping
            for row in reader:
                self.my_dict[(row['concept'], row['column'])] = {start_date: row['start_date'],
                                                                 end_date: row['end_date'],
                                                                 concept_modified: row['concept_modified']}
        return self.my_dict
