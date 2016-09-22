import csv
import collections
import re
import itertools
f = open('/home/nash/ayushi/n_abd.txt', 'r')
rows = [line.split("\t") for line in f.readlines()]

# function to get the names of unique (although repeated) class labels
def get_namesegments(rows):
    name_segments = []
    for i in range(len(rows) - 1):
        if rows[i][13] != rows[i + 1][13]:
            name_segments.append(rows[i][13] + '_' + str(i))
    return name_segments

# getting their indexes
def get_indexsegments(rows):
    index = []
    for i in range(len(rows) - 1):
        if rows[i][13] != rows[i + 1][13]:
           index.append(i)
    return index

# creating a dic with names as keys and [] as value
def create_dic():
    dic = collections.OrderedDict()
    nlist = get_namesegments(rows)
    dic = dict((key, []) for key in nlist)
    return dic

# chunking the file based on the length of each element in the index
def chunk_file():
    sliced_rows = []
    index = get_indexsegments(rows)
    print len(index)
    dict = create_dic()
    start = 0
    for i in index:
        end = i
        sliced = rows[start:end]
        start = i + 1
        sliced_rows.append(sliced)
    return sliced_rows
# getting the first six

def get_first():
    concatenated = []
    slices = chunk_file()
    for i in slices:
        slices_six = i[:6] 
        for row in slices_six:
            concatenated += row  # here's where I can't concatenate the nested rows
            # you are concatenating the first six rows from ALL slices to the same list! is that right? no. 
#            print concatenated

def get_first_new():
    list_of_concatenated_rows = []
    slices = chunk_file()
    for segment in slices:
        concatenated_row = []
        top6 = segment[:6]
        vowel = [frame for sublist in top6 for frame in sublist]
        #print vowel            
        list_of_concatenated_rows.append(vowel)
    return list_of_concatenated_rows

print "printing"        
conc_rows = get_first_new()
print len(conc_rows)

with open('n_abd_frames.csv', 'w') as csvfile:
    for row in conc_rows:
        csvfile.write("\t".join([str(e) for e in row]) + "\n")

#with open('n_abd_frames.csv', 'wb') as csvfile:
 #    for ele in conc_rows:
  #       csvfile.writelines(ele)
print "Done"
