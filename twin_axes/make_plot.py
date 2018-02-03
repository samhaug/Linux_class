#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : make_plot.py
Purpose : ---
Creation Date : 03-02-2018
Last Modified : Sat 03 Feb 2018 05:16:10 PM EST
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import MultipleLocator



def main():
    ax_202,ax_199 = setup_figure()
    cat_bank,values = read_hg_csv('Hg_isotopedata_forSam.csv')
    line_202 = ax_202.scatter(0,float(cat_bank[1]),
                              marker='D',c='gray',
                              lw=1,edgecolor='k',s=100)
    line_199 = ax_199.scatter(100,float(cat_bank[2]),
                              marker='o',c='gray',
                              lw=1,edgecolor='w',s=100)
    line_199.set_clip_on(False)
    line_202.set_clip_on(False)

    for ii in values:
        v = ii.strip().split(',')
        ax_202.scatter(float(v[-1]),float(v[2]),
                       s=150,c='steelblue',marker='o')
        ax_202.scatter(float(v[-1]),float(v[1]),
                       s=150,c='maroon',marker='D')



    plt.savefig('make_plot.pdf')
    plt.show()

def read_hg_csv(fname):
    hg_list = open(fname,'r').readlines()
    cat_bank = hg_list[2].strip().split(',')
    values = hg_list[3::]
    return cat_bank,values

def setup_figure():
    x_ml = MultipleLocator(5)
    ax_202_ml = MultipleLocator(0.1)
    font = {'family': 'serif',
            'color':  'black',
            'weight': 'heavy',
            'size': 14}

    fig,ax_202 = plt.subplots(figsize=(6,4))

    ax_202.set_xlim(0,100)
    ax_202.set_xlabel('% Distance Through Reactor Bed',fontdict=font)
    # Make second axis on top of first, and have them share the X axis
    ax_199 = ax_202.twinx()
    ax_199.set_xlim(0,100)
    ax_202.set_ylim(-2,1)
    ax_199.set_ylim(-2,1)
    ax_202.set_ylabel(r'$\delta^{202}$ Hg $(\perthousand)$',fontdict=font)
    ax_199.set_ylabel(r'$\Delta^{199}$ Hg $(\perthousand)$',fontdict=font)
    ax_202.tick_params(axis='y',labelsize=8)
    ax_202.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    ax_199.tick_params(axis='y',labelsize=8)
    ax_199.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    ax_202.tick_params(axis='x',labelsize=8)
    ax_202.xaxis.set_minor_locator(x_ml)
    ax_202.yaxis.set_minor_locator(ax_202_ml)
    plt.tight_layout()

    return ax_202,ax_199

main()
