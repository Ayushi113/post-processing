import collections
import re
import itertools
f = open('sample_paste2.txt', 'r')
rows = [line.split("\t") for line in f.readlines()]

# function to get the names of unique (although repeated) class labels


def get_namesegments(rows):
    name_segments = []
    for i in range(len(rows) - 1):
        if rows[i][12] != rows[i + 1][12]:
            name_segments.append(rows[i][12] + '_' + str(i))
    return name_segments

# getting their indexes


def get_indexsegments(rows):
    index = []
    for i in range(len(rows) - 1):
        if rows[i][12] != rows[i + 1][12]:
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
    dict = create_dic()
    start = 0
    for i in index:
        end = i
        sliced = rows[start:end]
        start = i + 1
        sliced_rows.append(sliced)
    return sliced_rows
# getting the first six


# see, you have the list of top six rows, yes.
# yes
# that gets flattened to a concatenated row? yes
# all those concatenated rows must be collected in a list?
# that list gets returned.
# so, a list of lists.
# flatten the list of concatenated rows?!
# yeah, ideally a list of lists. but right now we need to flatten it.
# where are we missing this. okay, let me send you the file?
# a list of list of lists actually, we must flatten and concatenate this list of lists
def get_first():
    concatenated = []
    slices = chunk_file()

    for i in slices:
        slices_six = i[:6]
        for row in slices_six:
            concatenated += row  # here's where I can't concatenate the nested rows
            # you are concatenating the first six rows from ALL slices to the same list! is that right? no.
            print concatenated


def get_first_new():
    list_of_concatenated_rows = []
    slices = chunk_file()
    for segment in slices:
        # one concatenated row per segment
        concatenated_row = []
        top6 = segment[:6]
        for row in top6:
            concatenated_row += row
        list_of_concatenated_rows.append(concatenated_row)
    return list_of_concatenated_rows  # should work i think
# print get_namesegments(rows)
# print get_indexsegments(rows)
# print create_dic()
print get_first_new()
