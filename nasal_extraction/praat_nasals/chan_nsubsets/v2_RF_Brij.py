#usr/bin/env/python
import numpy as np
import sklearn
import matplotlib.pyplot as plt
from sklearn import manifold
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter
from sklearn.cross_validation import cross_val_score
from sklearn.datasets import make_blobs
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix

X = []
Y = []
vowel_array = []
dir_array = {'NV':1, 'VN':2 }

with open('/home/nash/ayushi/Projects_2016/nasals_Jan16/scripts/python_postproc/nasal_extraction/praat_nasals/chan_nsubsets/chan_m_praat.csv') as fil:
     for line in fil.read().splitlines():
         sp = line.split(',')
         print sp
 	 feat_vector = sp[2:34]+ [dir_array[sp[36]]]
         if sp[1] not in vowel_array:
 	    vowel_array.append(sp[1])
         Y.append(vowel_array.index(sp[1]))
         X.append(feat_vector)

X = np.array(X, dtype=float)
Y = np.array(Y, dtype=float)
#clf = (n_estimators=10, max_depth=None, min_samples_split=1, random_state=0)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)
lin_clf = svm.SVC(verbose=1, kernel = 'rbf')
lin_clf.fit(X_train, Y_train)
Y_predicted = lin_clf.predict(X_test)
scores = cross_val_score(lin_clf, X, Y, cv=5)
print scores
fig = plt.figure()
tsne = manifold.TSNE(n_components=2, init='pca', random_state=0)
LD = tsne.fit_transform(X)
plt.scatter(LD[:, 0], LD[:, 1], c=['b', 'r'], cmap=plt.cm.Spectral)
#ax.xaxis.set_major_formatter(NullFormatter())
#ax.yaxis.set_major_formatter(NullFormatter())
plt.axis('tight')
plt.show()

print(classification_report(Y_test, Y_predicted, target_names=vowel_array))
print confusion_matrix(Y_test, Y_predicted)

#print scores

 
         

