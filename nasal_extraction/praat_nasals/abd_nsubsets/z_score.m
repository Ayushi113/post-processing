cd '/home/nash/ayushi/Projects_2016/nasals_Jan16/scripts/python_postproc/nasal_extraction/praat_nasals/abd_nsubsets'


fid=fopen('abd_VN_praat.csv');
C=textscan(fid, '%s%s%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%f%s%s');
fclose(fid);

d=C(3:35);
[Z,mu,sigma] = zscore(cell2mat(d));
