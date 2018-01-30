#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : process_xrd.py
Purpose : Smooth, find peaks, plot
Creation Date : 14-01-2018
Last Modified : Tue 23 Jan 2018 07:21:43 PM EST
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator

from scipy.ndimage.filters import gaussian_filter
from scipy.signal import argrelextrema
from glob import glob
from subprocess import call

def main():
    fig,ax_list  = setup_figure()
    xray_info,data = read_data('./2M1-std2.TXT')
    find_peaks(data,ax_list[1])
    theta_range = data[:,0]

    spectra_list = []
    for ii in glob('./random_files/*'):
        xray_info,data = read_data(ii)
        spectra_list.append(data[:,1])

    average_spectra(theta_range,spectra_list,ax_list[0])
    plt.savefig('process_xrd.pdf')
    plt.show()

def average_spectra(theta_range,spectra_list,ax):
    mean = np.mean(spectra_list,axis=0)
    std = np.std(spectra_list,axis=0)
    ax.fill_between(theta_range,mean+std,mean-std,color='k',alpha=0.5,lw=0)
    ax.plot(theta_range,mean,lw=0.5,color='k')

def find_peaks(data,ax):
    g_1 = gaussian_filter(data[:,1],8)
    idx_max = argrelextrema(g_1,np.greater)[0]
    ax.plot(data[:,0],data[:,1],color='k',alpha=0.5,lw=0.7)
    ax.plot(data[:,0],g_1,lw=0.7)
    for ii in idx_max:
        ax.axvline(data[ii,0],color='k',alpha=0.7,lw=0.5)

def read_data(path_to_xrd_file):
    f = open(path_to_xrd_file).readlines()
    xray_info = f[7].strip().split('\t')[1]
    data = np.genfromtxt(path_to_xrd_file,skip_header=17)
    return xray_info,data

def setup_figure():
    fig,ax_list = plt.subplots(2,1,figsize=(8,5))
    plt.figtext(0.05,0.95,'(a)',size=14)
    plt.figtext(0.05,0.5,'(b)',size=14)
    ax_list[0].set_title('Averaging XRD spectra',size=14)
    ax_list[1].set_title('Peak finding with gaussian_filter',size=14)
    ax_list[1].set_xlabel(r'$2\Theta$',size=12)
    ax_list[0].xaxis.set_ticklabels([])
    minorLocator = MultipleLocator(1)
    for ax in ax_list.reshape(ax_list.size):
        ax.xaxis.set_minor_locator(minorLocator)
        ax.set_ylabel('Counts',size=12)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_ticks_position('bottom')
        ax.tick_params(axis='both', which='major', labelsize=7)
    return fig,ax_list

main()



