import csv
import collections
import re
import itertools
f = open('/Users/spl/Desktop/pen_drive/merged_all/merged_mega.csv', 'r')
rows = [line.split(" ") for line in f.readlines()]
print rows[1][13]
# function to get the names of unique (although repeated) class label
# getting their indexes
def get_indexsegments(rows):
    index = []
    for i in range(len(rows) - 1):
        if rows[i][13] != rows[i + 1][13]:
           index.append(i)
    return index

list_indexes = get_indexsegments(rows)
#print list_indexes

def get_timerange(list_ind):
    time_range = []
    for i in range(len(list_ind)-1):
        index = list_ind[i+1] - list_ind[i] 
        trange = range(1, index+1)
#        print trange
        chunk_size = len(trange)/3
 #       print chunk_size
        for j in range(1, len(trange)):
            if j < chunk_size:
               trange[j] = 1
#               print trange
#               return 1
            elif j >= chunk_size and j < chunk_size*2:
               trange[j] = 2
               #print trange
            elif j >= chunk_size*2 and j < chunk_size*3:
               trange[j] = 3
            elif j >= chunk_size*3:   
               trange[j] = 3
   #            print trange
        time_range.append(trange)
    return time_range

time_range = get_timerange(list_indexes)

with open('merged_timechunk.csv', 'w') as csvfile:
    for row in time_range:
        csvfile.write("\t".join([str(e) for e in row]) + "\n")
