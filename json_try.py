import json
from unicodedata import decimal
import numpy as np
import cv2 
import os
from os  import listdir
from os.path import isfile, join
import json
from decimal import *


def make_specialized_list(batch_size, Filename):


    test_list =  [[] for i in range(batch_size)]


    for i in range(0,batch_size):
        test_list[i].append(FileName[i])
        test_list[i].append(Decimal(i))
    

    return test_list




def text_write(final_list):
    for i in range(0,len(final_list)):
        final_list[i][0]  = str(final_list[i][0])
        final_list[i][1]  = str(final_list[i][1])
    for i in range(0,len(final_list)):
        with open("batchfile0.txt",'a+') as f:
            f.write( final_list[i][0] + " " +  final_list[i][1] +"\n")
            
        
       
def json_load(batch_size,tuple_list):
    # json 的資料形式字串
    for i in range(0,5):
        i = Decimal(i)
        x =  '{ tuple_list}'

    # 轉換json
    person = json.loads(x)

    print(type(person)) #<class 'dict'>
    print(person)#{'name': 'jim', 'age': 25, 'city': 'Taiwan'}
    print(person['age']) #25








#--------------------------------------------------------

folder_name = []
total_size = 0
data_path =r"C:\Users\Max\Desktop\python\programming\MLandDL\Training data" #target folder(parent)

for root, dirts, files in os.walk(data_path):
    for dirt in dirts:
        folder_name.append(dirt)
    total_size += len(files)

print("found", total_size, "file." )
print("folder:", folder_name) #list that store folder names,(folders means children)

#--------------------------------------------------------

file_list = []

batch_size = 100


for i in range(len(folder_name)):
    labelPath = data_path + r'\\' + folder_name[i]
    FileName = [f for f in listdir(labelPath) if isfile(join(labelPath, f))]
    tuple_list = make_specialized_list(batch_size, FileName)
    print(tuple_list)
    
    
#    text_write(tuple_list)
    
    
    
    

    for j in range(len(FileName)):
        path = labelPath + r'\\' + FileName[j]
    
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        
        file_list.append(img)
        

print(np.array(file_list).shape)

    


#--------------------------------------------------------
#json

# json 的資料形式字串
x =  '{ "name":"jim", "age":25, "city":"Taiwan"}'

# 轉換json
person = json.loads(x)

print(type(person)) #<class 'dict'>
print(person)#{'name': 'jim', 'age': 25, 'city': 'Taiwan'}
print(person['age']) #25










erson = {'name': 'jim', 'age': 25, 'city': 'Taiwan'}

data = json.dumps(person)

print(type(data)) #<class 'str'>
print(data) #{"name": "jim", "age": 25, "city": "Taiwan"}



# 寫入資料
#with open('data.json', 'w') as f:
#    json.dump(x, f)
 
# 讀取資料
#with open('data.json', 'r') as f:
#    data = json.load(f)

#-----------------------------------------------------

json_load(10)