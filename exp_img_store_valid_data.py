import sqlite3
import json
from unicodedata import decimal
import numpy as np
import cv2 
import os
from os  import listdir
from os.path import isfile, join
from decimal import *



FileName = []
file_list = []
total_size = 0
data_path =r"C:\Users\Max\Desktop\python\programming\MLandDL\Testing data"

for root, dirts, files in os.walk(data_path):
    for file in files:
        FileName.append(file)     
    total_size += len(files)


print("found", total_size, "file." )
    

valid_data = [[] for i in range(0,total_size)]

for i in range(total_size):


    valid_data[i].append(FileName[i])
    valid_data[i].append(i*0.1)
    
#--------------------------------------------------------


#print(valid_data)




















conn = sqlite3.connect('valid_data.db')
cursor = conn.cursor()


#create
cursor.execute('DROP TABLE IF EXISTS valid_data')
cursor.execute('CREATE TABLE IF NOT EXISTS valid_data('
               'valid_data_file_name STRING PRIMARY KEY not null, '
               'gtg_delay_avg FLOAT'
               ')')







#insert
insert_query = 'INSERT INTO valid_data VALUES(?, ?)'


#data_num = 2

#file_name = ['kirai','kirai1']
#delay_list = [0.5,0.4111111]


#valid_data = []



#for i in range(0,data_num):
#    valid_data.append((file_name[i],delay_list[i]))


cursor.executemany(insert_query, valid_data)


#select
for row in cursor.execute('Select * From valid_data'):
    print(row)





conn.commit()
conn.close()