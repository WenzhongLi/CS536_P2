#### CREATE train_RBF.pkl and test_RBF.pkl from train_PCA.pkl###

"""STUDENT CODE"""
import pickle
import numpy as np


train_cluster=pickle.load(open( "Kmean_cluster.pkl", "rb" ))
print(train_cluster)
#please do not re-generate the file 
#from sklearn.cluster import KMeans
#generated by KMeans(n_clusters=1000,init='random', random_state=10).fit(train_data['data'])

