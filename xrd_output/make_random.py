#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : make_random.py
Purpose : create a large dataset by modifying one file with random noise
Creation Date : 23-01-2018
Last Modified : Tue 23 Jan 2018 06:36:32 PM EST
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
from subprocess import call
import h5py



def main ():
    num_files = 50

    seed_file = '2M1-std2.TXT'
    random_directory = 'random_files'
    #Get array data from seed file
    seed_array = np.genfromtxt(seed_file,skip_header=17)
    #Make list of the first 17 lines (header data)
    seed_header = open(seed_file).readlines()[0:17]

    for ii in range(num_files):
        #make array of random floats between -1 and 1.
        r = np.random.uniform(-1,1,size=len(seed_array[:,1]))

        #multiply this by 1/2 the minimum value of 
        #the array to make a bed of noise.
        r *= seed_array[:,1].min()*0.5
        rand_seed = seed_array[:,1] + r

        #make name for new random file by modifying original name
        random_name = seed_file[0:7]+'-'+str(ii)+seed_file[8::]

        #transpose and stack 2theta and random arrays to make
        # array that is Nx2, where N is length of seed_array
        random_array = np.hstack((np.array([seed_array[:,0]]).T,
                                  np.array([rand_seed]).T))

        #write an identical header for each file and then 
        #write the array beneath

        with open(random_directory+'/'+random_name,'w') as f:
            for lines in seed_header:
                f.write(lines)
            #fmt '%8.3f' kwarg means 3 digit precision floating point 
            #with whitespace fill to 8 character spaces.
            np.savetxt(f,random_array,fmt='%8.3f')

main()

