#### CREATE train_RBF.pkl and test_RBF.pkl from train_PCA.pkl###

"""STUDENT CODE"""
import pickle
import math
import sys
import numpy as np

class RBF:

    def __init__(self, train_cluster, train_data):
        self.train_cluster = train_cluster
        self.train_data = train_data
        self.cluster = self.getCluster()

    def rbf(self, x, ave, sigma_2):
        return math.exp(-sum((x[i] - ave[i]) ** 2 for i in range(len(x))) / (2 * sigma_2))

    def getCluster(self):
        cluster = dict()
        for i in range(len(self.train_data['data'])):
            m = self.train_cluster[i]
            if m not in cluster:
                cluster[m] = dict()
                cluster[m]['points'] = []
            cluster[m]['points'].append(train_data['data'][i])
        j = 0
        for k in cluster:
            print('k=',k,'j=',j)
            j += 1
            average = [0] * len(self.train_data['data'][0])
            num = len(cluster[k]['points'])
            for temp in cluster[k]['points']:
                for i in range(len(temp)):
                    average[i] += temp[i]
            for i in range(len(average)):
                average[i] /= num
            cluster[k]['average'] = average
            min_dist = sys.maxsize
            for x in cluster[k]['points']:
                min_dist = min(min_dist, sum((x[i] - average[i]) ** 2 for i in range(len(x))))
            if min_dist == 0:
                min_dist = sys.maxsize
                for x in cluster[k]['points']:
                    dist = sum((x[i] - average[i]) ** 2 for i in range(len(x)))
                    if dist > 0 and dist < min_dist:
                        min_dist = dist
            cluster[k]['sigma_2'] = min_dist
        return cluster

    def getFi(self):
        fi = []
        count = 1
        for x in self.train_data['data']:
            print(count)
            count += 1
            temp = []
            for i in range(1000):
                temp.append(self.rbf(x,self.cluster[i]['average'], self.cluster[i]['sigma_2']))
            fi.append(temp)
        fi = np.asarray(fi)
        return fi

    def save(self, ratio):
        fi = self.getFi()
        trainNum = int(len(fi)*ratio)
        train_data_dict = dict(data=fi[:trainNum],target=self.train_data['target'][:trainNum])
        test_data_dict = dict(data=fi[trainNum:], target=self.train_data['target'][trainNum:])
        pickle.dump(train_data_dict,open('train_RBF.pkl','wb'))
        pickle.dump(test_data_dict, open('test_RBF.pkl', 'wb'))

if __name__ == '__main__':
    train_cluster=pickle.load(open( "Kmean_cluster.pkl", "rb" ), encoding='bytes')
    train_data = pickle.load(open("train_PCA.pkl", "rb"), encoding='bytes')
    train_data['data'] = train_data[b'data']
    train_data['target'] = train_data[b'target']
    r = RBF(train_cluster, train_data)
    r.save(0.5)

