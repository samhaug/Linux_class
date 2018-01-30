#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : plot_gephen.py
Purpose : reproduce scatter plot
Creation Date : 06-01-2018
Last Modified : Tue 23 Jan 2018 06:41:19 PM EST
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
from subprocess import call

def main():
    fig,ax = setup_figure()
    dist,S,std = read_data()
    ax.errorbar(dist,S,yerr=std,fmt='d',capthick=10,elinewidth=1)
    #plt.tight_layout()
    plt.show()
    #plt.savefig('plot_gephen.pdf')
    #call('evince plot_gephen.pdf',shell=True)

def read_data():
    d = np.genfromtxt('Gephen_Example.csv',skip_header=1,delimiter=',')
    dist = d[:,0]
    S = d[:,1]
    std = d[:,2]
    return dist,S,std

def setup_figure():
    fig,ax = plt.subplots(figsize=(4,4))
    ax.set_title('Transect 1',size=12)
    ax.set_xlabel(r'Distance from Pyrrhotite into apatite ($\mu m$)',size=10)
    ax.set_ylabel(r'S in apatite ($\mu g/g$)',size=10)
    ax.set_xlim(20,90)
    ax.set_ylim(0,400)
    ax.axhline(25,ls='--',c='k',alpha=0.5)
    ax.text(85,375,'A',size=20)
    ax.text(48,30,r'EPMA Limit of Detection 25 $\mu g/g$',size=8)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(axis='both', which='major', labelsize=7)
    ax.grid(alpha=0.3)
    return fig,ax

main()
