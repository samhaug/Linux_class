#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : plot_colormap.py
Purpose : demonstrate how to plot color images with colorbars
Creation Date : 07-03-2018
Last Modified : Wed 07 Mar 2018 10:58:28 AM EST
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
from subprocess import call
from os import listdir

def main():
    #Read in two shear wave models at 70 km and 125 km 
    dvs70 = np.genfromtxt('./dvs_70km.dat')
    dvs125 = np.genfromtxt('./dvs_125km.dat')
    easy_way(dvs70)

def quick_way(dvs):
    plt.imshow(dvs,cmap='coolwarm_r',aspect='auto',
               extent=[-180,180,-90,90])
    plt.xlabel(r'Longitude ($^\circ$)')
    plt.ylabel(r'Latitude ($^\circ$)')
    plt.colorbar(orientation='horizontal',label=r'$\delta V_{S}(\%)$')
    plt.show()

def proper_way(dvs):
    fig,ax = plt.subplots(figsize=()
    plt.imshow(dvs,cmap='coolwarm_r',aspect='auto',
               extent=[-180,180,-90,90])
    plt.xlabel(r'Longitude ($^\circ$)')
    plt.ylabel(r'Latitude ($^\circ$)')
    plt.colorbar(orientation='horizontal',label=r'$\delta V_{S}(\%)$')
    plt.show()

main()
