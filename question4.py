#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def run():
    np.random.seed(0)
    sets = np.random.randn(4,100)
    W_pbty = np.random.rand(4, 100)
    for d_index in range(4):
        YgivenX = []
        w = []
        for i in range(100):
            if W_pbty[d_index, i] > 0.5:
                w.append(1)
            else:
                w.append(-1)
        for i in range(100):
            YgivenX.append(sets[d_index, i] * w[i])
        # plt.plot(sets[d_index], YgivenX)  # 用上述生成的1000个xy值对生成1000个点
        # plt.show()  # 绘制图像
        f1 = plt.figure(1)
        plt.scatter(sets[d_index], YgivenX, color='#FFAA00',marker='*')
        plt.show()

        # x = sets[d_index]
        # y = YgivenX
        # slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        # y1 = []
        # for point_x in sets[d_index]:
        #     y1.append(point_x * slope + intercept)
        # plt.plot(x, y1, ms=10, label="c2")
        # plt.show()





if __name__ == "__main__":
    run()