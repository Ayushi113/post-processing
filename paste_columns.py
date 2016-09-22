f = open('/home/nash/ayushi/n_abd.txt', 'r')
rows = [line.split("\t") for line in f.readlines()]
class_collector = {}
for row in rows:
    # check if the class is in the container
    if row[13] not in class_collector:
        # add the current row if the class label isnt present
        class_collector[row[13]] = row
    else:
        # append if it is present
        class_collector[row[13]] += row
# done
