# Libraries
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets

import pandas as pd
import numpy as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

iris = datasets.load_iris()

# dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])
# print(iris.keys())

print(iris.data.shape)

# knn = KNeighborsClassifier(n_neighbors=6)
# knn.fit(iris['data'], iris['target'])

