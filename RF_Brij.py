#usr/bin/env/python

import sklearn
import numpy as np
X = []
Y = []
vowel_array = []
dir_array = {'NV':1, 'VN':2 }

with open('/home/nash/ayushi/Projects_2016/nasals_Jan16/scripts/matlab_featureext/WAV/MALE/abd_nfeats/aopo_backup') as fil:
     for line in fil.read().splitlines():
         sp = line.split()
#         print sp[14]
  	 feat_vector = sp[:11]+ [dir_array[sp[14]]]
         if sp[13] not in vowel_array:
 	    vowel_array.append(sp[13])
         Y.append(vowel_array.index(sp[13]))
         X.append(feat_vector)



 
         

