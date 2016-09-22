#usr/bin/env/python
import os
import re
import csv
import subprocess
from itertools import izip

inputdir = '/home/nash/ayushi/Projects_2016/nasals_Jan16/scripts/nasal_extraction/praat'
list_vowels = ['i', 'A', 'ee', 'oh', 'aa', 'E']
nasal_list = ['m', 'n']
def get_feats(indir):
    feats = [] 
    for file in os.listdir(indir):
        if file.endswith(".csv"):
           file = indir+'/'+file
           feats.append(file)
    return feats

def get_attributes(infor):
    attributes = []
    for index in range(len(infor)-1):
        char = infor[index].split(' ')
#        print char
        if char[1] in list_vowels:
           context_VC = infor[index+1]
           context_CV = infor[index-1]
           if context_VC in nasal_list:
              dir = "VN"
              nasal_consonant = context_VC
              vowel_attribute = [dir, nasal_consonant]
              attributes.append(vowel_attribute)
           elif context_CV in nasal_list:
              dir = "NV"
              nasal_consonant = context_VC
              vowel_attribute = [dir, nasal_consonant]
              attributes.append(vowel_attribute)
    return attributes

print get_attributes()
 
# def extract_rows(fil, inf):
#     nasal_frames = []
#     attributes = get_attributes(inf)
#     for line in attributes:
#         nasals = fil[line[0]:line[1]]
#         nasals = [row + ' ' + line[2] + ' ' + line[3] + ' ' + line[4] for row in nasals]
#         nasal_frames.append(nasals)
#     return nasal_frames

# def main_program():
#     feat_files = get_feats(inputdir)
#     inf_files = get_inf(inputdir)
#     for (feat, inf) in izip(feat_files, inf_files):
#         feats_read = open(feat).readlines()
#         inf_read = open(inf).readlines()
#         lines = extract_rows(feats_read, inf_read)
#         print lines
#         with open(feat.split()[0] + '.nfeats', 'wb') as inp:
#              writer = csv.writer(inp, delimiter =' ', skipinitialspace=True)      
#              writer.writerows(lines)
#         #f = open(filename.split()[0] + '.lab',"r")
#         #text_in = f.read()
#         #text_out = re.sub(r'"(?!")', '', text_in)            
#         #f = open(filename.split()[0] + '.lab',"wb")
#         #f.write(text_out)
#         print "Done"

working = main_program()
