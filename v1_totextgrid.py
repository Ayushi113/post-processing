#usr/bin/env/python

import os
print os.path.splitext("path_to_file")[0]

textgrid = open('/home/nash/ayushi/Projects_2016/nasals_Jan16/data/structure_textgrid.txt', 'r')
lab = open('/home/nash/ayushi/Projects_2016/nasals_Jan16/data/Bd_01.lab', 'r')

def create_intervals(lab_f):
    len_lab = len(lab_f.readlines())
    with open('Bd_01t.TextGrid2', 'a') as f1:
         for line in textgrid:
             f1.write(line)
         for i in range(len_lab):
             f1.write('class = "IntervalTier"\n')     
             f1.write('name = "Vowel"\n') 
             f1.write('xmin = 0\n') 
             f1.write('xmax = 5.617625\n') 
             f1.write('intervals: size = 16\n')
             f1.write('intervals [1]:\n')
             f1.write('xmin = 0\n')
             f1.write('xmax = 0\n')
             f1.write('text = """')
print 1
             
        
        
    
#    for line in textgrid:
         
            
    
    

create_intervals(lab)



