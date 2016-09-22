src_base1="/home/nash/ayushi/Projects_2016/nasals_Jan16/data/SHRUTI-Bangla Speech Corpus/WAV/MALE"
src_base2="/home/nash/ayushi/Projects_2016/nasals_Jan16/data/SHRUTI-Bangla Speech Corpus/WAV/FEMALE"
dest="/home/nash/ayushi/Projects_2016/nasals_Jan16/data/extracted_shortwav"
file=open('/home/nash/ayushi/Projects_2016/nasals_Jan16/scripts/names','r')
print 1
name_list=[]
for i in file:
	name_list.append(i)
print name_list[1:10]
import os
print 1
for i in name_list:
	folder=str.split(i,"_")[0]
	src=src_base1+'/'+folder
	print src
	if os.path.isdir(src)==False:
		src=src_base2+'/'+folder
	src_file=src+str.split(i,'\n')[0]+'.wav'
        print src_file
	if os.path.exists(src_file)==True:
		shutil.copy(src_file,dest)
		
print "done"
