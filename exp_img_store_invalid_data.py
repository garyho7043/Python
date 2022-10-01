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
data_path =r".\MLandDL\Testing data"

for root, dirts, files in os.walk(data_path):
    for file in files:
        FileName.append(file)     
    total_size += len(files)


print("found", total_size, "file." )
    

invalid_data = [[] for i in range(0,total_size)]

for i in range(total_size):


    invalid_data[i].append(FileName[i])
    invalid_data[i].append(0)
    
#--------------------------------------------------------


#print(invalid_data)

















conn = sqlite3.connect('invalid_data.db')
cursor = conn.cursor()




#create table
cursor.execute('DROP TABLE IF EXISTS invalid_data')
cursor.execute('CREATE TABLE IF NOT EXISTS invalid_data('
               'invalid_data_file_name STRING PRIMARY KEY not null ,'
               'gtg_delay_avg FLOAT'
               ')')







#insert
insert_query = 'INSERT INTO invalid_data VALUES(?,?)'




#invalid_data = [['kirai','a'],['kirai1',0]]


cursor.executemany(insert_query, invalid_data)






#select
for row in cursor.execute('Select * From invalid_data'):
    print(row)





conn.commit()
conn.close()










