# -*- coding: utf-8 -*-
"""
Created on Thu Nov  08 2018

@author: vianney
"""


class mapping_file_builder:

    def __init__(self, output_file_moda,output_file_entity):
        self.output_file_moda = output_file_moda
        self.output_file_entity = output_file_entity
        self.moda = [{
            "Entity": "Entity",
            "DataElementConcept": "DataElementConcept",
            "ColumnInFile": "ColumnInFile",
            "Modality": "Modality"
        }]
        self.entity = [{
            "Entity": "Entity",
            "FileName": "FileName"
        }]
        self.list_moda=[]
        self.list_entity=[]

    def addToModa(self, Entity, DataElementConcept,modality):
        if Entity + "|" + DataElementConcept not in self.list_moda:
            moda = {
                "Entity": Entity,
                "DataElementConcept": DataElementConcept,
                "ColumnInFile": "",
                "Modality": modality
            }
            self.moda.append(moda)
            self.list_moda.append(Entity + "|" + DataElementConcept)

    def addToEntiy(self, Entity):
        if Entity not in self.list_entity:
            entity = {
                "Entity": Entity,
                "FileName": ""
            }
            self.entity.append(entity)
            self.list_entity.append(Entity)

    def writeMappings(self):
        for moda in self.moda:
            self.output_file_moda.write(moda["Entity"] + "," + moda["DataElementConcept"] + ',' + moda["ColumnInFile"] + ',' + moda["Modality"] + '\n')
        for ent in self.entity:
            self.output_file_entity.write(ent["Entity"] + "," + ent['FileName'] + '\n')
