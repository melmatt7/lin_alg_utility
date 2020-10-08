#!/usr/bin/python
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
import pprint

def mono_interp(point_list):    
    pp = pprint.PrettyPrinter(indent=4)
    t = np.empty((len(point_list), 0), int)
    y = np.empty((len(point_list), 0), int)

    point_list = point_list.split()
    for point in point_list:
        xy = point.split(',')
        t = np.append(t, int(xy[0]))
        y = np.append(y, int(xy[1]))
    
    print('\n')
    A = np.vander(t,increasing=True)
    pp.pprint(A)

    print('\n')
    c = la.solve(A,y)
    pp.pprint(c)

    print('\np(t) = ', end = '')

    for i in range(len(c)):
        if c[i] == 0:
            continue

        if i > 0:
            print(' + ', end = '')
            
        print(c[i], 't^', i, sep="", end = '')
    print('\n')

mono_interp(point_list = input("Enter Points:\n"))