#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : sams_version.py
Purpose : Make Sam's version of Spencer's Mercury plot
Creation Date : 03-02-2018
Last Modified : Tue 06 Feb 2018 03:44:31 PM EST
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import MultipleLocator

def main():
    color_202 = '#d62728'
    color_199 = '#1f77b4'
    ax_202,ax_199 = setup_figure(color_202,color_199)
    cat_bank,d202,d199,percent_thru = read_hg_csv('Hg_isotopedata_forSam.csv')

    ax_202.scatter(percent_thru,d202,s=90,c=color_202,marker='D',
                   label=r'$\delta$202 Values',zorder=1)
    ax_199.scatter(percent_thru,d199,s=90,c=color_199,marker='o',
                   label=r'$\Delta$199 Values',zorder=1)
    #These lines add scatter points for catalyst blanks like original
    #ax_202.scatter(0,cat_bank[0],marker='D',c='k',s=100,
    #                          label=r'$\delta$202 Catalyst Blank')
    #ax_199.scatter(100,cat_bank[1],marker='o',c='k',s=100,
    #                          label=r'$\delta$202 Catalyst Blank')

    #Would horizontal lines be appropriate?
    ax_202.axhline(cat_bank[0],color=color_202,zorder=0,lw=0.5)
    ax_202.axhline(-0.33,color=color_199,zorder=0,lw=0.5)
    # Need to put 199 cat blank on ax_202 so overlap problems wont happen
    #ax_199.axhline(cat_bank[1],color=color_199,zorder=0,lw=0.5)
    ax_202.text(0,cat_bank[0]+0.05,'$\delta$202 Catalyst Blank',
               color=color_202,size=8)
    ax_199.text(70,cat_bank[1]-0.011,'$\Delta$199 Catalyst Blank',
               color=color_199,size=8)

    plt.savefig('sams_version.pdf')
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

def setup_figure(color_202,color_199):
    fig,ax_202 = plt.subplots(figsize=(6,4))

    # Make second axis on top of first, and have them share the X axis.
    # twinx() clones the axes and places it on top of the original.
    ax_199 = ax_202.twinx()

    ax_202.set_xlabel('% Distance through reactor bed',size=12)
    ax_202.set_ylabel(r'$\delta^{202}$ Hg $(\perthousand)$',size=12)
    ax_199.set_ylabel(r'$\Delta^{199}$ Hg $(\perthousand)$',size=12)

    ax_199.spines['right'].set_linewidth(1.0)
    ax_199.spines['right'].set_color(color_199)
    ax_199.spines['left'].set_color(color_202)

    ax_202.spines['left'].set_linewidth(1.0)
    ax_202.spines['left'].set_color(color_202)
    ax_202.spines['right'].set_color(color_199)

    ax_202.spines['top'].set_visible(False)
    ax_199.spines['top'].set_visible(False)

    ax_199.yaxis.label.set_color(color_199)
    ax_202.yaxis.label.set_color(color_202)

    ax_199.set_xlim(-5,105)
    ax_202.set_ylim(-2,1.1)
    ax_199.set_ylim(0,.26)

    # Set decimal precision on tick labels
    # %.2f means floating poing with 2 decimal precision
    ax_202.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    ax_199.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

    #adjusting increment of minor ticks. See imports at top
    x_ml = MultipleLocator(5)
    ax_202_ml = MultipleLocator(0.1)
    ax_199_ml = MultipleLocator(0.01)

    ax_202.xaxis.set_minor_locator(x_ml)
    ax_202.yaxis.set_minor_locator(ax_202_ml)
    ax_199.yaxis.set_minor_locator(ax_199_ml)

    ax_199.tick_params(axis='y',which='both',colors=color_199,labelsize=8)
    ax_202.tick_params(axis='y',which='both',colors=color_202,labelsize=8)
    ax_202.tick_params(axis='x',which='both',labelsize=8)


    #Optional call makes axes stretch to sides of figure
    plt.tight_layout()

    return ax_202,ax_199

main()
