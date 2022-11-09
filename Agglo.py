import numpy as np
from scipy.cluster import hierarchy as h
from scipy.spatial import distance as d
import matplotlib.pyplot as plt

points=[(18,0),(22,0),(43,0),(42,0),(27,0),(25,0)]
names=['p1','p2','p3','p4','p5','p6']

x=d.pdist(points,'euclidean')

temp = h.linkage(x,'single')
plt.figure()

dn= h.dendrogram(temp,labels=names)

plt.show()