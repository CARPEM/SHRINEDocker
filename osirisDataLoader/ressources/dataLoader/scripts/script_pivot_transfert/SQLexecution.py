# -*- coding: utf-8 -*-
"""
Created 2018/01/05

@author: David BAUDOIN

fonction : script d'interaction avec la base de donnees i2b2

"""

import psycopg2
import cx_Oracle as cx
# import mysql.connector

class i2b2_interaction:

    # construction de l'objet
    def __init__(self, type_connection, DB_host, DB_name, DB_port, BD_user, DB_password):
        self.type_connection = type_connection
        self.DB_host = DB_host
        self.DB_name = DB_name
        self.DB_port = DB_port
        self.BD_user = BD_user
        self.DB_password = DB_password

    def connect_i2b2(self):
        if self.type_connection.lower() == 'postgresql':
            config = 'host=' + self.DB_host + ' port=' + self.DB_port + ' dbname=' + self.DB_name + ' user=' + self.BD_user + ' password=' + self.DB_password
            dbcon = psycopg2.connect(config)
            dbcon.autocommit = True
            cur = dbcon.cursor()
            return cur

        elif self.type_connection.lower() == 'oracle':
            dsn = cx.makedsn(self.DB_host, self.DB_port, sid='CDWEGP')
            dbcon = cx.connect(self.BD_user, self.DB_password, dsn)
            dbcon.autocommit = True
            cur = dbcon.cursor()
            return cur

        elif self.type_connection.lower() == 'mysql':
            dbcon = mysql.connector.connect(user=self.BD_user, database=self.DB_name, password=self.DB_password, host=self.DB_host, port=self.DB_port)
            dbcon.autocommit = True
            cur = dbcon.cursor()
            return cur

        return None

    def executeBasicRequest(self, request_i2b2):
        res = []
        cursor = self.connect_i2b2()
        cursor.execute(request_i2b2.encode('utf-8'))
        # return a dictionnary :
        # dic[concept1] = [(patient24, value24), (patient30, value30), ...]
        for row in cursor:
            res.append((str(row[0]), str(row[1])))
        cursor.close()
        return res

    def executeBasicRequest_n(self, request_i2b2, number_of_var):
        res = []
        cursor = self.connect_i2b2()
        cursor.execute(request_i2b2.encode('utf-8'))
        # return a dictionnary :
        # dic[concept1] = [(patient24, value24), (patient30, value30), ...]
        for row in cursor:
            tuple_resp = []
            for i in range(0, number_of_var):
                tuple_resp.append(str(row[i]))
            #print (tuple_resp)
            res.append(tuple_resp)
        cursor.close()
        return res

    def insert_data(self, request_i2b2, values):
        cursor = self.connect_i2b2()
        #print(request_i2b2)
        #print(values)
        if not None in values :
            cursor.execute(request_i2b2.encode('utf-8'), values)
        cursor.close()

    def executeBasicRequestWithDate(self, request_i2b2):
        res = [];resp_patient=[]
        cursor = self.connect_i2b2()
        print (request_i2b2.encode('utf-8'))
        cursor.execute(request_i2b2.encode('utf-8'))
        # return a dictionnary :
        # dic[concept1] = [(patient24, value24), (patient30, value30), (patient30, value31), ...]
        for row in cursor:
            if str(row[0]) not in resp_patient:
                resp_patient.append(str(row[0]))
                res.append((str(row[0]), str(row[1])))
        cursor.close()
        return res

    def executeRequestWithRepetition(self, request_i2b2):
        # imput value [(patient, value, group_value), ...]
        res = [];resp_patient=[];resp_group=[]
        #print(request_i2b2.encode('utf-8'))
        cursor = self.connect_i2b2()
        cursor.execute(request_i2b2.encode('utf-8'))
        # return a dictionnary :
        # dic[concept1] = [(patient24, repeat_instr, repeat_inst, value24), (patient30, repeat_instr, repeat_inst, value30), (patient30, repeat_instr, repeat_inst, value31), ...]
        for row in cursor:
            if str(row[0]) not in resp_patient:
                resp_patient.append(str(row[0]))
                resp_group.append(str(row[1]))
                res.append((str(row[0]), str(row[1]), str(row[2])))
            elif str(row[1]) not in resp_group:
                resp_group.append(str(row[1]))
                res.append((str(row[0]), str(row[1]), str(row[2])))
        cursor.close()
        return res
