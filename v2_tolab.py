#usr/bin/env/python
import os
import re
import csv
import subprocess
from itertools import izip

inputdir = '/home/nash/ayushi/Projects_2016/nasals_Jan16/data/textgrids_wav'
print 1
def get_textgrids(indir):
    textgrids = [] 
    for file in os.listdir(indir):
        if file.endswith(".TextGrid"):
           file = indir+'/'+file
           textgrids.append(file)
    return textgrids

def get_lines(fil):
    durations = []
    for i in fil:
        if "xmax" in i or "xmin" in i or "text" in i or "size" in i:
            durations.append(i)
    return durations

def get_phones(lis):
    phone = []
    for line in lis:
        char = line.split(' ')      
        if char[0] == "\t\t\t\ttext":
           char[2] = char[2][:-1]
           phone.append(char[2])
    return phone

def get_durations(lis):
    dur = []
    for line in lis:
        char = line.split(' ')
        if char[0] == "\t\t\t\txmax":
           char[2] = char[2][:-1]
           dur.append(char[2])
    return dur

def main_program():
    indir = get_textgrids(inputdir)
    print 1
    for filename in indir:
        text_read = open(filename).readlines()
        lines = get_lines(text_read)
        durations = get_durations(lines)
        phones = get_phones(lines)
        phones = [i.replace('"',' ') for i in phones]
        middle = [100 for i in range(len(phones))]
        with open(filename.split()[0] + '.lab', 'wb') as inp:
             writer = csv.writer(inp, delimiter =' ', skipinitialspace=True)      
             writer.writerows(izip(durations, middle, phones))
        f = open(filename.split()[0] + '.lab',"r")
        text_in = f.read()
        text_out = re.sub(r'"(?!")', '', text_in)            
        f = open(filename.split()[0] + '.lab',"wb")
        f.write(text_out)
        print "Done"

working = main_program()
