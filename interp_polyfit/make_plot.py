#!/home/samhaug/anaconda3/bin/python

'''
==============================================================================

File Name : make_plot.py
Purpose : Reproduce first plot in diagrams.pdf
Creation Date : 30-01-2018
Last Modified : Wed 31 Jan 2018 11:14:42 AM EST
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection


def main():
    fig,ax = setup_figure()
    plt.figtext(0.05,0.9,'A',size=20)
    ax.text(0.084092,1.413547,'Skarn',size=12)
    ax.text(1.95006,0.43502,'Fe-Ti,V',size=12)
    #rotated Skarn/Porphyry text
    ax.text(0.72314,5.70849,'Skarn',size=12,rotation=65,
            backgroundcolor='white')
    ax.text(1.52314,5.70849,'Porphyry',size=12,rotation=65,
            backgroundcolor='white')
    ax.text(2.52314,4.50849,'(Nadoli et al.\nsubmitted)',size=8,rotation=65,
            backgroundcolor='white')

    plot_red_triangles(ax,'red_triangle_coords')
    plot_green_triangles(ax,'green_triangle_coords')
    plot_yellow_squares(ax,'yellow_square_coords')
    plot_purple_diamonds(ax,'purple_diamond_coords')
    plot_blue_circles(ax,'dark_blue_circle_coords',alpha=1.0)
    plot_blue_circles(ax,'light_blue_circle_coords',alpha=0.3)

    fit_skarn_porphyry(ax,'skarn_porphyry_curve')

    horiz = np.genfromtxt('horizontal_line',delimiter=',')
    ax.plot(horiz[:,0],horiz[:,1],color='k',lw=2)

    slant = np.genfromtxt('slant_line',delimiter=',')
    ax.plot(slant[:,0],slant[:,1],color='k',lw=2)

    plot_porphyry_poly(ax,'porphyry_coords')
    plot_IOGC_poly(ax,'IOGC_coords')
    plot_BIF_poly(ax,'BIF_coords')
    plot_kiruna_poly(ax,'kiruna_coords')
    plt.savefig('al_mn_plot.pdf')

    plt.show()

def plot_porphyry_poly(ax,fname):
    coords = np.genfromtxt(fname,delimiter=',')
    polygon = Polygon(coords,True)
    p = PatchCollection([polygon],lw=2,facecolor='none',
                         edgecolor='k')
    ax.annotate('Porphyry',xy=(0.67334,0.24271),xytext=(1.60416,0.17219),size=12,
            arrowprops=dict(facecolor='black',width=0.5,headwidth=3,
                            headlength=5))
    ax.add_collection(p)

def plot_kiruna_poly(ax,fname):
    coords = np.genfromtxt(fname,delimiter=',')
    polygon = Polygon(coords,True)
    p = PatchCollection([polygon],lw=2,facecolor='none',
                         edgecolor='k',linestyle='-')
    ax.annotate('Kiruna',xy=(0.34484,0.08374),xytext=(0.149122,0.03315),size=12,
            arrowprops=dict(facecolor='black',width=0.5,headwidth=3,
                            headlength=5))
    ax.add_collection(p)

def plot_BIF_poly(ax,fname):
    coords = np.genfromtxt(fname,delimiter=',')
    polygon = Polygon(coords,True)
    p = PatchCollection([polygon],lw=1.5,facecolor='none',
                         edgecolor='k',linestyle='--')
    ax.add_collection(p)
    ax.text(0.02261,0.054844,'BIF',size=12)

def plot_IOGC_poly(ax,fname):
    coords = np.genfromtxt(fname,delimiter=',')
    polygon = Polygon(coords,True)
    p = PatchCollection([polygon],lw=2,facecolor='none',edgecolor='k')
    ax.add_collection(p)
    ax.annotate('IOGC',xy=(0.067246,0.155347),xytext=(0.011401,0.170237),
                size=12,arrowprops=dict(facecolor='black',width=0.5,
                                        headwidth=3,headlength=5))

def fit_skarn_porphyry(ax,fname):
    coords = np.genfromtxt(fname,delimiter=',')
    # example of how to interpolate
    f = interp1d(coords[:,0],coords[:,1])
    # make uniform coordinate space for x range
    newx = np.linspace(coords[0,0],coords[-1,0],num=100)

    #ax.plot(coords[:,0],coords[:,1],ls='--',c='r',alpha=0.5)
    # plot the interpolated values
    #ax.plot(newx,f(newx),ls='-',c='r',alpha=0.5)

    # z will be array of polynomial coeffs for arbitrary degree
    z = np.polyfit(coords[:,0],coords[:,1],deg=5)
    # the poly1d object will evaluate the polynomial at any point(s)
    p = np.poly1d(z)
    # plot the new polynomial over the uniform linspace of x values
    ax.plot(newx,p(newx),ls='--',c='k',lw=2)

def plot_red_triangles(ax,fname):
    coords = np.genfromtxt(fname,delimiter=',')
    ax.scatter(coords[:,0],coords[:,1],marker='v',color='r',facecolors='none',
              edgecolors='firebrick',s=60,alpha=0.6,rasterized=False)
    ax.scatter(np.mean(coords[:,0]),np.mean(coords[:,1]),marker='+',s=500,
               color='firebrick')

def plot_green_triangles(ax,fname):
    coords = np.genfromtxt(fname,delimiter=',')
    ax.scatter(coords[:,0],coords[:,1],marker='^',facecolors='none',
              edgecolors='olive',s=60,alpha=0.6,rasterized=False)
    ax.scatter(np.mean(coords[:,0]),np.mean(coords[:,1]),marker='+',s=500,
               color='olive')

def plot_yellow_squares(ax,fname):
    coords = np.genfromtxt(fname,delimiter=',')
    ax.scatter(coords[:,0],coords[:,1],marker='s',facecolors='none',
              edgecolors='goldenrod',s=60,alpha=0.6,rasterized=False)
    ax.scatter(np.mean(coords[:,0]),np.mean(coords[:,1]),marker='+',s=500,
               color='goldenrod')

def plot_blue_circles(ax,fname,alpha):
    coords = np.genfromtxt(fname,delimiter=',')
    ax.scatter(coords[:,0],coords[:,1],marker='o',facecolors='none',
              edgecolors='steelblue',s=60,alpha=alpha,rasterized=False)
    ax.scatter(np.mean(coords[:,0]),np.mean(coords[:,1]),marker='+',s=500,
               color='steelblue')

def plot_purple_diamonds(ax,fname):
    coords = np.genfromtxt(fname,delimiter=',')
    ax.scatter(coords[:,0],coords[:,1],marker='d',facecolors='none',
              edgecolors='purple',s=60,alpha=1.0,rasterized=False)
    ax.scatter(np.mean(coords[:,0]),np.mean(coords[:,1]),marker='+',s=500,
               color='purple')

def setup_figure():
    fig,ax = plt.subplots(figsize=(7,7))
    ax.set_xscale("log", nonposx='clip')
    ax.set_yscale("log", nonposy='clip')
    ax.set_xlim(0.0001,10)
    #needs a dummy label in front, Not sure why?
    ax.set_xticklabels(['fuck',0.0001,0.001,0.01,0.1,1,10])
    ax.set_ylim(0.001,10)
    ax.set_yticklabels(['fuck',0.001,0.01,0.1,1,10])
    ax.set_xlabel('Ti+V (wt%)',size=14)
    ax.set_ylabel('Al+Mn (wt%)',size=14)
    ax.grid(ls='--',color='k',alpha=0.7)
    return fig,ax


main()
