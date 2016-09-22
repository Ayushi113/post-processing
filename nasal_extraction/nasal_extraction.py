#usr/bin/env/python
import os
import re
import csv
import subprocess
from itertools import izip

inputdir = '/home/nash/ayushi/Projects_2016/nasals_Jan16/scripts/nasal_extraction'
#outputdir = '/home/nash/ayushi/Projects_2016/nasals_Jan16/data/shruti_corpus/textgrids_all/labs'
def get_inf(indir):
    infs = [] 
    for file in os.listdir(indir):
        if file.endswith(".inff"):
           file = indir+'/'+file
           infs.append(file)
    return infs

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
        if char[0] == "preciding_vowel:":
           dir = "VN"
           context = infor[index+1]
           context = context[-3]
           phb, phe, vowel = int(char[1]), int(char[3]), char[5][:-2]
           vowel_attribute = [phb, phe, vowel, dir, context]
           attributes.append(vowel_attribute)
        elif char[0] == "succeeding_vowel:":
             dir = "NV"
             context = infor[index-1]
             context = context[-3]
             phb, phe, vowel = int(char[1]), int(char[3]), char[5][:-2]
             vowel_attribute = [phb, phe, vowel, dir, context]
             attributes.append(vowel_attribute)
    return attributes
 
def extract_rows(fil, inf):
    nasal_frames = []
    attributes = get_attributes(inf)
    for line in attributes:
        nasals = fil[line[0]:line[1]]
        nasals = [row + ' ' + line[2] + ' ' + line[3] + ' ' + line[4] for row in nasals]
        nasal_frames.append(nasals)
    return nasal_frames

def main_program():
    feat_files = get_feats(inputdir)
    inf_files = get_inf(inputdir)
    for (feat, inf) in izip(feat_files, inf_files):
        feats_read = open(feat).readlines()
        inf_read = open(inf).readlines()
        lines = extract_rows(feats_read, inf_read)
        print lines
        with open(feat.split()[0] + '.nfeats', 'wb') as inp:
             writer = csv.writer(inp, delimiter =' ', skipinitialspace=True)      
             writer.writerows(lines)
        #f = open(filename.split()[0] + '.lab',"r")
        #text_in = f.read()
        #text_out = re.sub(r'"(?!")', '', text_in)            
        #f = open(filename.split()[0] + '.lab',"wb")
        #f.write(text_out)
        print "Done"

working = main_program()
