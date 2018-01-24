#!/home/samhaug/anaconda2/bin/python

'''
============================================================================== 
File Name : xrd_statistics.py
Purpose : Find mean,min,max,std,etc of group of xrd 'runs'
Creation Date : 23-01-2018
Last Modified : Tue 23 Jan 2018 06:41:24 PM EST
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
from glob import glob

def main():

    spectra_list = []
    for fname in glob('random_files/*'):
        a = np.genfromtxt(fname,skip_header=17)[:,1]
        spectra_list.append(a)
    print np.array(spectra_list).shape

    #print('max')
    #print(np.max(spectra_list,axis=0))
    #print('min')
    #print(np.min(spectra_list,axis=0))
    #print('std')
    #print(np.std(spectra_list,axis=0))
    #print('mean')
    #print(np.mean(spectra_list,axis=0))


main()
