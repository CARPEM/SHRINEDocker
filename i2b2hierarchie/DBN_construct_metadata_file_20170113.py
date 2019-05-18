# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29

@author: david
"""
import re

class constuct_metadata_file:

    # construction de l'objet
    def __init__(self, config_name, nameTable):
        self.config_name = config_name
        self.nameTable = nameTable
        self.tabConfig = []
        self.lect_config_name()


    def lect_config_name (self) :
        f_config = open(self.config_name, 'r')
        find = False
        for line in f_config :
            if find :
                self.tabConfig = line.replace('\n', '').replace('\r', '').split(';')
                break
            if line.replace('\n', '').replace('\r', '') == self.nameTable :
                find = True

        if not find : print (self.nameTable + ' is not found')
        f_config.close()


    def add_title_csvfile (self) :
        value = ''
        for config in self.tabConfig :
            if re.search('[.*]', config) :
                value += config[0:config.index('[')] + ';'
            else : value += config + ';'
        value = value[:-1] + '\n'
        return value

    def add_node_csvfile (self, tab_info) :
        value = ''
        pattern = "\[.*\]"
        for conf in self.tabConfig :
            m = re.search(pattern, conf)
            if re.search(pattern, conf) :
                value += self.lect_change_var(m.group(0), conf, tab_info[conf[0:conf.index('[')]]) + ';'
            else : value += tab_info [conf] + ';'
        value = value[:-1] + '\n'
        return value

    def lect_change_var (self, match_modif, variable, info) :
        #value = info
        new_value = ''
        modif_value = variable[variable.index('['):].replace('[', '').replace(']', '').split(',')
        for modif in modif_value :
            if re.search('@', modif) :
                new_value += info
            elif modif[0] == '\'' :
                new_value += modif.replace('\'', '')
        return new_value
