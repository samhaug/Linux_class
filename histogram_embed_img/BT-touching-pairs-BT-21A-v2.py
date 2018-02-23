#!/home/samhaug/anaconda2/bin/python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
=========================================================
4 part figure for touching pairs of oxides in Bishop Tuff samples
February 13 2018
James Jolles
=========================================================
'''

import matplotlib.pyplot as plt
#from nplib import scolor, splot2
#import pandas as pd
import numpy as np
from matplotlib.ticker import MultipleLocator
import matplotlib.image as mpimg

fig = plt.figure(figsize=(4.5,4))

#reading data and setting bins
d = np.genfromtxt('BT-touching-pairs.csv',skip_header=1,delimiter=',')
t = np.genfromtxt('BT-TEMPS-NNO.csv',skip_header=1,delimiter=',')
binBoundariesTMTE = np.linspace(7,9.5,26)
binBoundariesILM = np.linspace(43,48,51)
binBoundariesTEMP = np.linspace(680,840,161)

#Text lines at ylim * 7/8 and ylim * 3/4 seem good
#Subplot for TMTE
ax1 = fig.add_subplot(221)
n, bins, patches = ax1.hist(d[:,4],color='r',bins=binBoundariesTMTE)
ax1.set_xlabel('TiO$_2$ (wt%)',size='10')
ax1.set_ylabel('Number of Analyses', size='9.5')
ax1.text(7.1,8.75,'TMTE',size=9)
ax1.text(7.1,7.5,'n = 24',size=9)
ax1_ml = MultipleLocator(0.5)
ax1.xaxis.set_minor_locator(ax1_ml)
ax1.tick_params(axis='both', which='major', labelsize=8,)
ax1.set_ylim([0,10])
ax1.yaxis.set_ticks(np.arange(0,11,5))
ax1.set_xlim([7,9.5])
ax1.xaxis.set_ticks(np.arange(7,9.6,0.5))
#black bar on the plots
ax1.axhline(y=5,xmin=.32,xmax=.88,color='k',linewidth=4,alpha=1)
ax1.text(8.3,5.5,'TiO$_2$ range',size='8',ha='center')

#Subplot for ILM
ax2 = fig.add_subplot(222)
n, bins, patches = ax2.hist(d[:,5],color='r',bins=binBoundariesILM)
ax2.set_xlabel('TiO$_2$ (wt%)',size='10')
ax2.text(43.2,2.625,'ILM',size='9')
ax2.text(43.2,2.25,'n = 9',size='9')
ax2_ml = MultipleLocator(0.5)
ax2.xaxis.set_minor_locator(ax2_ml)
ax2.tick_params(axis='both', which='major', labelsize=8)
ax2.set_ylim([0,3])
ax2.set_xlim([43,48])
ax2.xaxis.set_ticks(np.arange(43,48.1,1))
ax2.axhline(y=2.3,xmin=.4,xmax=.74,color='k',linewidth=4,alpha=1)
ax2.text(45.9,2.5,'TiO$_2$ range',size='8',ha='center')

#Subplot for BSE image
ax3 = fig.add_subplot(223)
img = mpimg.imread('BT-21A-15-touching-pair.png')
imgplot = plt.imshow(img)
ax3.text(50,100,'Ig2NWa',color='w',size='9')
ax3.axis('off')

#subplot for temperature histogram
ax4 = fig.add_subplot(224)
n, bins, patches = ax4.hist(t[:,2],color='grey',alpha=0.5,bins=binBoundariesTEMP)
n, bins, patches = ax4.hist(d[:,6],color='r',bins=binBoundariesTEMP)
ax4.set_xlabel('Temperature ($^\circ$C)',size='10')
ax4.text(686.4,52.25,r'787$\pm$12$^\circ$C', size='9')
ax4.text(686.4,45,'216 pairs', size='9')
ax4_ml = MultipleLocator(5)
ax4.xaxis.set_minor_locator(ax4_ml)
ax4.tick_params(axis='both', which='major', labelsize=8)
ax4.set_ylim([0,60])
ax4.set_xlim([680,840])
ax4.xaxis.set_ticks(np.arange(680,841,40))

#drawing fig and saving it
fig1 = plt.gcf()
plt.tight_layout()
plt.show()
plt.draw()
fig1.savefig('Figs2/BT-21A-touching-pairs-v2.png',dpi=300)



