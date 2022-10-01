import cv2 
import os
from os  import listdir
from os.path import isfile, join



def open_picture(img):

    cv2.imshow('experience_data', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()





FileName = []
file_list = []
total_size = 0
data_path =r".\MLandDL\Testing data"

for root, dirts, files in os.walk(data_path):
    for file in files:
        FileName.append(file)     
    total_size += len(files)


print("found", total_size, "file." )
    

for j in range(len(FileName)):
    path = data_path + r'\\' + FileName[j]
    
    img = cv2.imread(path, cv2.IMREAD_COLOR) 
    file_list.append(img)
    
     
#   open_picture(img)

 #analysis part------------------------------------------------------------------       
        
        
        
 #-------------------------------------------------------------------------------        

open_picture(file_list[0])
     
     
     
     
     
      
