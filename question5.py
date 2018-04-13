#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''

import numpy as np
import matplotlib.pyplot as plt
import math

def func0(x):
    group_pred = []
    for pred in x:
        r = 0
        if pred < 0.5:
            r = 0
        elif pred >= 0.5 and pred < 1.5:
            r = 1
        elif pred >= 1.5 and pred < 2.5:
            r = 2
        elif pred >= 2.5:
            r = 3
        group_pred.append(r)
    return np.array(group_pred)


def q5():
    # x = np.linspace(-0.5, 3.5)
    x = np.linspace(0, 4)
    y0 = func0(x)
    fig, ax = plt.subplots()
    plt.plot(x, y0, 'b', linewidth=1)
    plt.ylim(ymin=0)
    plt.show()


def q7():
    e = math.e
    train = [0.99617486338797812, 0.99617486338797812, 0.99617486338797812, 0.99617486338797812, 0.99617486338797812,
             0.99562841530054647, 0.86284153005464481, 0.75027322404371588, 0.69180327868852454, 0.29234972677595628,
             0.23442622950819672]
    test = [0.51724137931034486, 0.51724137931034486, 0.51724137931034486, 0.51724137931034486, 0.51724137931034486,
            0.54187192118226601, 0.70935960591133007, 0.64039408866995073, 0.62561576354679804, 0.2413793103448276,
            0.25123152709359609]
    L = [0.00000001, e ** -25, e ** -20, e ** -15, e ** -10, e ** -5, 1, 2, 3, e ** 5, e ** 10]
    logL = np.log(L)
    plt.plot(logL, train, 'g', linewidth=2)
    plt.plot(logL, test, 'r', linewidth=2)
    plt.ylim(ymin=0)
    plt.show()

def q6():
    e = math.e
    train = [0.77339901477832518, 0.77339901477832518, 0.77339901477832518, 0.77339901477832518, 0.77339901477832518,
             0.84729064039408863, 0.98029556650246308, 0.98029556650246308, 0.97536945812807885, 0.66995073891625612,
             0.4039408866995074]
    test = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.99945355191256835, 0.99781420765027318, 0.99453551912568305,
            0.69781420765027324, 0.46010928961748632]
    L = [0.0000001, e ** -25, e ** -20, e ** -15, e ** -10, e ** -5, 1, 2, 3, e ** 5, e ** 10]
    logL = np.log(L)
    plt.plot(logL, train, 'r', linewidth=1)
    plt.plot(logL, test, 'g', linewidth=1)
    plt.ylim(ymin=0)
    plt.show()

if __name__ == "__main__":
    q6()


