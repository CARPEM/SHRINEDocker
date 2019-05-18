# -*- coding: utf-8 -*-
"""
Created on Thu Nov  08 2018

@author: vianney
"""

import os

class adapter_mapping_builder:

    def __init__(self, input_file,adapter_file):
        self.input_file = input_file
        self.adapter_file = adapter_file


    def lecture_file_i2b2(self) :
        i2b2meta= open(self.input_file,'r')

        try:
            os.remove(self.adapter_file)
        except OSError:
            pass
        adapter= open(self.adapter_file,'w')


        for line in i2b2meta :
            fullname = line.split(";")[1]
            # print(fullname)
            adapter.write("\"\\\\OSIRIS"+fullname.replace('\\\\','\\')+"\",\"\\\\OSIRIS"+fullname.replace('\\\\','\\')+"\"\n")
        i2b2meta.close()
