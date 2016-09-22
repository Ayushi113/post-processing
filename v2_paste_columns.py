import collections
import re
import itertools
f = open('/home/nash/ayushi/n_abd.txt', 'r')
rows = [line.split("\t") for line in f.readlines()]

#function to get the names of unique (although repeated) class labels
def get_namesegments(rows):
    name_segments = []
    for i in range(len(rows)-1):
        if rows[i][13] != rows[i+1][13]:
           name_segments.append(rows[i][13] + '_' + str(i))
    return name_segments
#getting their indexes
def get_indexsegments(rows):
    index = []
    for i in range(len(rows)-1):
        if rows[i][13] != rows[i+1][13]:
           index.append(i)
    return index
#creating a dic with names as keys and [] as value
def create_dic():
    dic = collections.OrderedDict()
    nlist = get_namesegments(rows)
    dic = dict((key, []) for key in nlist)
    return dic

# chunking the file based on the length of each element in the index
def chunk_file():
    sliced_rows = []
    index = get_indexsegments(rows)
    dict = create_dic()
    start = 0
    for i in index:       
        end = i
        sliced = rows[start:end]
        start = i+1
        sliced_rows.append(sliced)
    return sliced_rows
# getting the first six    
def get_first():
    concatenated = []
    slices = chunk_file()
    print slices[1]
    for i in slices:
        slices_six = i[:6]
        #print slices_six[1]
        for row in slices_six:
            concatenated += row #here's where I can't concatenate the nested rows
#            print concatenated
            
#print get_namesegments()
#print get_indexsegments()
#print create_dic()
k= get_first()
print k
