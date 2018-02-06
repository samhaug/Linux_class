#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : make_plot.py
Purpose : Reproduce Spencer's Mercury plot
Creation Date : 03-02-2018
Last Modified : Tue 06 Feb 2018 11:16:28 AM EST
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import MultipleLocator



def main():
    ax_202,ax_199 = setup_figure()
    cat_bank,d202,d199,percent_thru = read_hg_csv('Hg_isotopedata_forSam.csv')

    ax_202.scatter(percent_thru,d202,s=150,c='maroon',marker='D',
                   edgecolor='k',lw=1,label=r'$\delta$202 Values')
    line_202 = ax_202.scatter(0,cat_bank[0],
                              marker='D',c='gray',
                              lw=1,edgecolor='k',s=100,
                              label=r'$\delta$202 Catalyst Blank')
    line_199 = ax_199.scatter(100,cat_bank[1],
                              marker='o',c='gray',
                              lw=1,edgecolor='w',s=100,
                              label=r'$\Delta$199 Catalyst Blank')
    ax_202.scatter(percent_thru[0],d199[0]+3,s=150,c='royalblue',marker='o',
                   edgecolor='k',lw=1,label=r'$\Delta$199 Values')

    line_202 = ax_202.scatter(100,3,
                              marker='o',c='gray',
                              lw=1,edgecolor='w',s=100,
                              label=r'$\Delta$199 Catalyst Blank')
    line_199.set_clip_on(False)
    line_202.set_clip_on(False)
    ax_199.scatter(percent_thru,d199,s=150,c='royalblue',marker='o',
                   edgecolor='k',lw=1,label=r'$\Delta$199 Values')

    #handles,labels = ax_202.get_legend_handles_labels()
    font = {'family': 'serif',
            'color':  'black',
            'size': 10}
    legend = ax_202.legend(loc='upper right',fontdict=font,borderaxespad=0,
                            markerscale=0.8)
    legend.get_frame().set_edgecolor('k')

    plt.savefig('make_plot.pdf')
    plt.show()

def read_hg_csv(fname):
    hg_list = open(fname,'r').readlines()
    cat_bank = [float(i) for i in hg_list[2].strip().split(',')[1:3]]
    values = hg_list[3::]
    #Cannot begin variable name with number, i.e. no 202d, must be d202
    d202 = [float(i.strip().split(',')[1]) for i in hg_list[3::]]
    d199 = [float(i.strip().split(',')[2]) for i in hg_list[3::]]
    percent_thru = [float(i.strip().split(',')[3]) for i in hg_list[3::]]
    return cat_bank,d202,d199,percent_thru

def setup_figure():
    fig,ax_202 = plt.subplots(figsize=(8,5))

    # Make second axis on top of first, and have them share the X axis.
    # twinx() clones the axes and places it on top of the original.
    ax_199 = ax_202.twinx()

    # Make fontdict for axeslabels
    font = {'family': 'serif',
            'color':  'black',
            'weight': 'heavy',
            'size': 14}
    ax_202.set_xlabel('% Distance Through Reactor Bed',fontdict=font)
    ax_202.set_ylabel(r'$\delta^{202}$ Hg $(\perthousand)$',fontdict=font)
    ax_199.set_ylabel(r'$\Delta^{199}$ Hg $(\perthousand)$',fontdict=font)

    # Tried to make spines invisible so markers could be placed on top.
    #ax_199.spines['right'].set_visible(False)
    #ax_202.spines['left'].set_visible(False)

    # Make all but top axes spine and tickmark thin and grey
    for direction in ['bottom','left','right']:
          ax_199.spines[direction].set_linewidth(0.5)
          ax_199.spines[direction].set_color('grey')
          ax_202.spines[direction].set_linewidth(0.5)
          ax_202.spines[direction].set_color('grey')

    # Adjusting xlim and ylim because I can't figure out how to plot
    # markers over the axes spines
    ax_199.set_xlim(-5,105)
    ax_202.set_ylim(-2,1.05)
    ax_199.set_ylim(0,.26)

    # These are the limits from Spencer's original plot
    #ax_202.set_ylim(-2,1)
    #ax_199.set_ylim(0,.25)
    #ax_199.set_xlim(0,100)

    #Setting size of tick labels
    ax_202.tick_params(axis='y',labelsize=8)
    ax_199.tick_params(axis='y',labelsize=8)
    ax_202.tick_params(axis='x',labelsize=8)

    # Set decimal precision on tick labels
    # %.2f means floating poing with 2 decimal precision
    ax_202.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    ax_199.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

    #adjusting increment of minor ticks. See imports at top
    x_ml = MultipleLocator(5)
    ax_202_ml = MultipleLocator(0.1)
    ax_202.xaxis.set_minor_locator(x_ml)
    ax_202.yaxis.set_minor_locator(ax_202_ml)

    #Optional call makes axes stretch to sides of figure
    plt.tight_layout()

    return ax_202,ax_199

main()
