
'''
==============================================================================

File Name : plot_colormap.py
Purpose : demonstrate how to plot color images with colorbars
Creation Date : 07-03-2018
Last Modified : Sun 18 Mar 2018 04:38:44 PM EDT
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec


def main():
    '''
    #Read in two shear wave models at 70 km and 125 km 
    '''
    dvs70 = np.genfromtxt('./dvs_70km.dat')
    dvs125 = np.genfromtxt('./dvs_125km.dat')
    #quick_way(dvs70)
    #proper_way(dvs70)
    #using_gridspec(dvs70)
    two_subplots(dvs70,dvs125)

def quick_way(dvs):
    plt.imshow(dvs,cmap='coolwarm_r',aspect='auto',
               extent=[-180,180,-90,90])
    plt.xlabel(r'Longitude ($^\circ$)')
    plt.ylabel(r'Latitude ($^\circ$)')
    plt.colorbar(orientation='horizontal',label=r'$\delta V_{S}(\%)$')
    plt.show()

def proper_way(dvs):
    fig,ax = plt.subplots(figsize=(4,4))
    ax.set_xlabel(r'Longitude ($^\circ$)')
    ax.set_ylabel(r'Latitude ($^\circ$)')
    #add_axes([bottom left x, bottom left y, width, height])
    #add_axes in figure coordinates
    cbar_ax = fig.add_axes([0.27, 0.8, 0.5, 0.05])
    im = ax.imshow(dvs,cmap='coolwarm_r',aspect='auto',
               extent=[-180,180,-90,90])
    fig.colorbar(im,cax=cbar_ax,orientation='horizontal',label=r'$\delta V_{S}(\%)$')
    plt.show()

def using_gridspec(dvs):
    fig = plt.figure(figsize=(5.5,4))
    gs = gridspec.GridSpec(100,100)
    ax = plt.subplot(gs[:,0:85])
    cbar_ax = plt.subplot(gs[:,87:90])
    cbar_ax.tick_params(axis='both',which='major',labelsize=8)
    ax.tick_params(axis='both',which='major',labelsize=8)
    ax.set_xlabel(r'Longitude ($^\circ$)')
    ax.set_ylabel(r'Latitude ($^\circ$)')
    im = ax.imshow(dvs,cmap='coolwarm_r',aspect='auto',
               extent=[-180,180,-90,90])
    fig.colorbar(im,cax=cbar_ax,orientation='vertical',label=r'$\delta V_{S}(\%)$')
    plt.show()

def two_subplots(dvs1,dvs2):
    fig = plt.figure(figsize=(5.5,8))
    gs = gridspec.GridSpec(100,100)
    ax1 = plt.subplot(gs[0:40,:])
    ax2 = plt.subplot(gs[43:83:,:])
    cbar_ax = plt.subplot(gs[90:93,:])
    cbar_ax.tick_params(axis='both',which='major',labelsize=8)
    ax1.tick_params(axis='both',which='major',labelsize=8)
    ax1.get_xaxis().set_ticks([])
    ax2.tick_params(axis='both',which='major',labelsize=8)
    ax2.set_xlabel(r'Longitude ($^\circ$)')
    ax1.set_ylabel(r'Latitude ($^\circ$)')
    ax2.set_ylabel(r'Latitude ($^\circ$)')
    im = ax1.imshow(dvs1,cmap='coolwarm_r',aspect='auto',
               extent=[-180,180,-90,90])
    im = ax2.imshow(dvs2,cmap='coolwarm_r',aspect='auto',
               extent=[-180,180,-90,90])
    fig.colorbar(im,cax=cbar_ax,orientation='horizontal',label=r'$\delta V_{S}(\%)$')
    plt.show()

main()



