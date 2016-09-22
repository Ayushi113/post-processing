#usr/bin/env/python
import os
import re
import csv
import subprocess
from itertools import izip

inputdir = '/home/nash/ayushi/Projects_2016/nasals_Jan16/data/shruti_corpus/textgrids_all/textgrids'
#outputdir = '/home/nash/ayushi/Projects_2016/nasals_Jan16/data/shruti_corpus/textgrids_all/labs'
def get_textgrids(indir):
    textgrids = [] 
    for file in os.listdir(indir):
        if file.endswith(".TextGrid"):
           file = indir+'/'+file
           textgrids.append(file)
    return textgrids

def get_lines(fil):
    lines = []
    for i in fil:
        if "xmax" in i or "xmin" in i or "text" in i or "size" in i:
            lines.append(i)
    return lines

def size_intervals(fil):
    for i in range(len(fil)):
        if "phones" in fil[i]:
            seed = fil[i+3]
            size = seed.split(' ')[-1]
    return int(size)

def get_phones(lis):
    phone = []
    for line in lis:
        char = line.split(' ')
        print char
        if char[0] == "\t\t\t\t\t\ttext":
           ph = char[2][:-1]
           phone.append(ph)
    return phone

def get_durations(lis):
    dur = []
    for line in lis:
        char = line.split(' ')
        if char[0] == "\t\t\t\t\t\txmax":
           char[2] = char[2][:-1]
           dur.append(char[2])
    return dur

def main_program():
    indir = get_textgrids(inputdir)
    print indir
    for filename in indir:
        text_read = open(filename).readlines()
        interval = size_intervals(text_read)
        lines = get_lines(text_read)
        lines = [i.replace('  ','\t') for i in lines]
        print lines
        durations = get_durations(lines)[0:interval]
        phones = get_phones(lines)[0:interval]
        phones = [i.replace('"',' ') for i in phones]
        middle = [100 for i in range(len(phones))]
        print phones, durations
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
