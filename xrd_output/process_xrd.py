#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : process_xrd.py
Purpose : Smooth, find peaks, plot
Creation Date : 14-01-2018
Last Modified : Tue 23 Jan 2018 10:55:46 AM EST
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from scipy.ndimage.filters import gaussian_filter
from scipy.signal import argrelextrema
from matplotlib import pyplot as plt

def main():
    xray_info,data = read_data('./2M1-std2.TXT')
    g_1 = gaussian_filter(data[:,1],8)
    idx_max = argrelextrema(g_1,np.greater)[0]

    plt.plot(data[:,0],data[:,1],color='k',alpha=0.5)
    plt.plot(data[:,0],g_1)
    for ii in idx_max:
        plt.axvline(data[ii,0],color='k',alpha=0.3)
    plt.show()

def read_data(path_to_xrd_file):
    f = open(path_to_xrd_file).readlines()
    xray_info = f[7].strip().split('\t')[1]
    data = np.genfromtxt(path_to_xrd_file,skip_header=17)
    return xray_info,data


main()
