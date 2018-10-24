# -*- coding: utf-8 -*-
"""
Created 2018/01/03

@author: David BAUDOIN

fonction : script lisant les fichier csv ou de type csv et renvoyant un dictionnaire le contenu sous la forme :
    Dic_var[var1]=[data11, data12, ...]
    Dic_var[var2]=[data21, data22, ...]
    ...
"""

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