import numpy as np
import cv2 
import os
from os  import listdir
from os.path import isfile, join


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


for i in range(len(folder_name)):
    labelPath = data_path + r'\\' + folder_name[i]
    FileName = [f for f in listdir(labelPath) if isfile(join(labelPath, f))]
    

    for j in range(len(FileName)):
        path = labelPath + r'\\' + FileName[j]
    
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        
        file_list.append(img)
        

print(np.array(file_list).shape)

    


#--------------------------------------------------------