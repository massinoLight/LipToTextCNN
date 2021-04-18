from extract_lip import *

PATH = '/home/massino/Bureau/M1BigData/s2/FouilleDonnées/projet/LipReadingCNN/dataset/dataset/F01/words/01/01' 

image_list = os.listdir(PATH)


i=0
for image_name in image_list: 
  
  extract_lip(PATH+'/'+image_name,i)
  i=i+1
