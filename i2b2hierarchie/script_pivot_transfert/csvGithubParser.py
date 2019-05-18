#!/usr/bin/env python
# coding: utf-8


"""
Module description
"""

import argparse
import pandas as pd
import os

__author__ = "Antunes Mathias"
__version__ = "0.1.0"

ConceptualDomain_file_name = 'ConceptualDomain_data.tsv'
DataElementConcept_file_name = 'DataElementConcept_data.tsv'

#local files path
ConceptualDomain_local_file_path = 'OSIRIS-1.1.05/ConceptualDomain.tsv'
DataElementConcept_local_file_path = 'OSIRIS-1.1.05/DataElementConcept.tsv'

# try:
#     # Try to customize VARIABLES by reading them from config_tsvreader.py
#     from .config import *
# except ImportError as ex:
#     print("No config_tsvreader.py file found.")

parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.dirname(os.path.abspath(__file__))

abspath_ConceptualDomain_data = os.path.join(path, ConceptualDomain_file_name)
abspath_ConceptualDomain_local_file_path =  os.path.join(path, ConceptualDomain_local_file_path)
abspath_DataElementConcept_local_file_path = os.path.join(path, DataElementConcept_local_file_path)

def get_tsv_reader_clean():
    '''
    Read from gitHub OSIRIS ConceptualDomain and return a clean Pandas dataframe with only usefull columns

    :return: write a csv file and return pandas dataframe
    :rtype: pandas dataframe
    '''

    # If clean local file exists
    if not os.path.exists(abspath_ConceptualDomain_data):

        try:
            # Reading from Github data
            dfCD = pd.read_csv('https://raw.githubusercontent.com/siric-osiris/OSIRIS/v1.x/data/ConceptualDomain.tsv',
                               sep='\t', header=0)
        except:
            print('Couldn\'t reach ConceptualDomain data on github, data used may be outdated')
            # Read file separator tabulation, and header line 0.
            try:
                dfCD = pd.read_csv(abspath_ConceptualDomain_local_file_path, sep='\t', header=0)
            except Exception as e:
                raise e
        try:
            # Reading from Github data
            dfDEC = pd.read_csv(
                'https://raw.githubusercontent.com/siric-osiris/OSIRIS/v1.x/data/DataElementConcept.tsv', sep='\t',
                header=0)
        except:
            print('Couldn\'t reach DataElementConcept data on github, data used may be outdated')
            # Read file separator tabulation, and header line 0.
            try:
                dfDEC = pd.read_csv(abspath_DataElementConcept_local_file_path, sep='\t', header=0)
            except Exception as e:
                raise e
        # Name of the columns selected for the new tsv
        dfcd_clean = dfCD[['ValueMeaning', 'LabelValueMeaning', 'ConceptualDomain']]

        dfDEC_clean = dfDEC[['ConceptualDomain', 'DataElementConcept']]

        dfFinal = pd.merge(dfcd_clean, dfDEC_clean, on='ConceptualDomain')

        dfFinal_clean = dfFinal[['ValueMeaning', 'LabelValueMeaning', 'DataElementConcept']]

        dfFinal_clean['dataelementconcept_lower'] = pd.Series(dfFinal_clean['DataElementConcept'].str.lower(),
                                                              index=dfFinal_clean.index)

        # Writing tsv_clean file in current repository with tabulation separator and UTF-8 encoding
        dfFinal_clean.to_csv(abspath_ConceptualDomain_data, sep='\t', encoding='utf-8',
                             index=False)

        print("ConceptualDomain_data successfully created")

    else:

        # Read clean local file
        dfFinal_clean = pd.read_csv(abspath_ConceptualDomain_data, sep='\t', header=0)

        print("ConceptualDomain_data successfully read")

    return (dfFinal_clean)

def remove_ConceptualDomain_data():
    try:
        os.remove(abspath_ConceptualDomain_data)
    except Exception as e:
        raise FileNotFoundError(e)

def get_osiris_value_for_data_element_concept(dataelementconcept):
    '''

    :param ObjectClass: ex : Patient
    :param ObjectProperty:  ex : Gender
    :return: array of json of all possible values ex :  [{'code': 'HL7:F', 'Label': 'Female'}, {'code': 'HL7:M', 'Label': 'Male'},{...}]
    '''
    DataElementConcept = 'DataElementConcept'
    dataelementconcept_lower = 'dataelementconcept_lower'
    response = []

    # TSV file  getting from package osiris_tsvreader
    reader = get_tsv_reader_clean()
    # reader.set_index(DataElementConcept, inplace=True)

    dataelementconcept = dataelementconcept.lower()

    try:
        selected_data = reader.loc[reader[dataelementconcept_lower]==dataelementconcept]
    except Exception:
        try:
            remove_ConceptualDomain_data()
            reader = get_tsv_reader_clean()
            # reader.set_index(DataElementConcept, inplace=True)
            selected_data = reader.loc[reader[dataelementconcept_lower]==dataelementconcept]
            # print(reader)
        except Exception as e:
            print(e)
            return "Couldn't find " + str(dataelementconcept) + " in DataElementConcept "

    try:
        # Iteration with iterrows from Pandas
        for index, row in selected_data.iterrows():

            myjson = make_json(row)
            print(row)
            if myjson:
                response.append(myjson)
    except Exception as e:
        print(e)
        return []
    return response

def get_osiris_label_value(ObjectClass, ObjectProperty):
    '''

    :param ObjectClass: ex : Patient
    :param ObjectProperty:  ex : Gender
    :return: array of json of all possible values ex :  [{'code': 'HL7:F', 'Label': 'Female'}, {'code': 'HL7:M', 'Label': 'Male'},{...}]
    '''
    DataElementConcept = 'DataElementConcept'
    dataelementconcept_lower = 'dataelementconcept_lower'
    response = []

    # TSV file  getting from package osiris_tsvreader
    reader = get_tsv_reader_clean()
    # reader.set_index(DataElementConcept, inplace=True)

    dataelementconcept = str(ObjectClass).lower()+'_'+str(ObjectProperty).lower()

    try:
        selected_data = reader.loc[reader[dataelementconcept_lower]==dataelementconcept]
    except Exception:
        try:
            remove_ConceptualDomain_data()
            reader = get_tsv_reader_clean()
            # reader.set_index(DataElementConcept, inplace=True)
            selected_data = reader.loc[reader[dataelementconcept_lower]==dataelementconcept]
            # print(reader)
        except Exception as e:
            print(e)
            return "Couldn't find " + str(dataelementconcept) + " in DataElementConcept "

    try:
        # Iteration with iterrows from Pandas
        for index, row in selected_data.iterrows():

            myjson = make_json(row)

            if myjson:
                response.append(myjson)
    except Exception as e:
        print(e)
        return []
    return response


def make_json(row):
    """

    :param row: current row in tsv file
    :return: return json {"code":"LabelValue","Label": "LabelValueMeaning"}
    """
    # A json per result
    myjson = {

        # Dumping Osiris ID and LabelValueMeaning : ex({"value":"ValueMeaning","label": "LabelValueMeaning"})
        "code": row['ValueMeaning'],
        "Label": row['LabelValueMeaning']

    }

    # Appending in response's array ex(([json1,json2,...])
    return (myjson)
