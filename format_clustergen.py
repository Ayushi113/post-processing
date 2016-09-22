#usr/bin/env/python
import re
import pickle

def form_clgen(string):
    rem_reps = re.sub("\((2)\)", "", string)
    rem_prnths = re.search('\((.*?)\)',rem_reps).group(1)
    cnv_str = re.sub("</?s>|\((.*?)\)|\\r|\\n", "", string)
    cnv_str.rstrip()
    return rem_prnths + cnv_str

shruti_trans = open('/home/nash/ayushi/Projects_2016/nasals_Jan16/data/short_sent.txt', 'r')

def file_clgen(fil):
    lin_clg = []
    list_clg = fil.readlines()
    for i in list_clg:
        sent_clg = '( ' + form_clgen(i) + ')'
        lin_clg.append(sent_clg)
    return lin_clg

format = file_clgen(shruti_trans)

outfile = open('/home/nash/ayushi/Projects_2016/nasals_Jan16/data/txt.done.data.txt', 'w')
outfile.write("\n".join(format))

print "done"
