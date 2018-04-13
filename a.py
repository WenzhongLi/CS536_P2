#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''

import numpy as np

vector1 = np.array([1.0,2.0,3.0])
vector2 = np.array([1.0,2.0,3.0])
g = []
g.append([1,2,3,4])
g.append([1,2,3,4])

dis = np.linalg.norm(vector1 - vector2)
mu = np.mean(g,axis=0)
print dis == 0.0
print mu