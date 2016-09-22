#usr/bin/env/python
import os
import re
import csv
import subprocess
from itertools import izip

infile = open('/home/nash/ayushi/Projects_2016/nasals_Jan16/scripts/python_postproc/nasal_extraction/praat_nasals/chan_nsubsets/chan_final_praat.csv', 'r').readlines()
list_vowels = ['i', 'A', 'ee', 'oh', 'aa', 'E', 'oi']
nasal_list = ['m', 'n']

def get_feats(indir):
    feats = [] 
    for file in os.listdir(indir):
        if file.endswith(".csv"):
           file = indir+'/'+file
           feats.append(file)
    return feats

#feature_files = get_feats(inputdir)

def get_attributes(infor):
    attributes = []
    for index in range(1, len(infor)-1):
        char = infor[index].split(',')
        pr_char = infor[index-1].split(',')
        po_char = infor[index+1].split(',')
#        print char[1]
        if char[1] in list_vowels:
           context_VC = pr_char[1]
           context_CV = po_char[1]
           if context_VC in nasal_list:
              dir = "VN"
              nasal_consonant = context_VC
              print dir, nasal_consonant, index
              vowel_attribute = [dir, nasal_consonant]
              print vowel_attribute
              attributes.append(vowel_attribute)
           elif context_CV in nasal_list:
              dir = "NV"
              nasal_consonant = context_CV
              vowel_attribute = [dir, nasal_consonant]
              print vowel_attribute
              attributes.append(vowel_attribute)
           else:
              continue
    return 1

#print get_attributes(infile)
 
def extract_rows(inf):
    nasal_frames = []
     #attributes = get_attributes(inf)
    for index in range(1, len(inf)-1):
        char = inf[index].split(',')
        pr_char = inf[index-1].split(',')
        po_char = inf[index+1].split(',')
#        print char[1]
        if char[1] in list_vowels:
           if pr_char[1] in nasal_list:
              char.extend((pr_char[1], "NV"))
              nasal_frames.append(char)
           elif po_char[1] in nasal_list:
                #print char[1], index
                char.extend((po_char[1], "VN"))
                nasal_frames.append(char)

    return nasal_frames
nasal_rows = extract_rows(infile)
print nasal_rows

with open('nasals_praat_chan.csv', 'w') as csvfile:
    for row in nasal_rows:
        csvfile.write("\t".join([str(e) for e in row]) + "\n")
