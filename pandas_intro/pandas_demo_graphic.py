#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : pandas_demo.py
Purpose : Introduce some basic pandas functionalities
Creation Date : 14-02-2018
Last Modified : Wed 14 Feb 2018 12:32:49 PM EST
Created By : Samuel M. Haugland

   ▄███████▄    ▄████████ ███▄▄▄▄   ████████▄     ▄████████
  ███    ███   ███    ███ ███▀▀▀██▄ ███   ▀███   ███    ███
  ███    ███   ███    ███ ███   ███ ███    ███   ███    ███
  ███    ███   ███    ███ ███   ███ ███    ███   ███    ███
▀█████████▀  ▀███████████ ███   ███ ███    ███ ▀███████████
  ███          ███    ███ ███   ███ ███    ███   ███    ███
  ███          ███    ███ ███   ███ ███   ▄███   ███    ███
 ▄████▀        ███    █▀   ▀█   █▀  ████████▀    ███    █▀
   ▄███████▄  ▄██████▄   ▄█     █▄     ▄████████    ▄████████
  ███    ███ ███    ███ ███     ███   ███    ███   ███    ███
  ███    ███ ███    ███ ███     ███   ███    █▀    ███    ███
  ███    ███ ███    ███ ███     ███  ▄███▄▄▄      ▄███▄▄▄▄██▀
▀█████████▀  ███    ███ ███     ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀
  ███        ███    ███ ███     ███   ███    █▄  ▀███████████
  ███        ███    ███ ███ ▄█▄ ███   ███    ███   ███    ███
 ▄████▀       ▀██████▀   ▀███▀███▀    ██████████   ███    ███
                                                   ███    ███

The library’s name derives from PAnel DAta,
a common term for multidimensional data sets
encountered in statistics and econometrics.

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


# Read excel file to DataFrame object
df = pandas.read_excel('appendixB.xlsx',header=2)
df_3 = pandas.read_excel('appendixB.xlsx',header=3)

# Dataframe objects are just concatenated series objects, a series is a single
# column
s = df[df.columns[0]]
s = df['Study']
# Find unique studies
u = df['Study'].unique()

#return first ten rows
first_ten = df.head(10)

#return last ten rows
last_ten = df.tail(10)

#return dataframe without column
df_drop = df.drop('Study',axis=1)

#return dataframe with columns renamed
#rename = df.rename(columns={'oldname':'newname',
#                            'oldname':'newname'})
rename = df.rename(columns={'Study':'STUDY',
                            'sample #':'Sample_no'})

# return dataframe of only study and sample column
study_sample = df[['Study','sample #']]

# Boolean indexing of dataframe object
takahashi = df.loc[df['Study']=='Takahashi, 1978']

# & means 'and', | means 'or'
# Index all studies by takahashi,1978 that also have xtal phases 'gl+ol'
takahashi = df.loc[(df['Study']=='Takahashi, 1978') &
                   (df['xtal phases']=='gl+ol')]

# Index all studies by takahashi,1978 or studies that have gl+ol+sp as xtal phase
takahashi_or_glolsp = df.loc[(df['Study']=='Takahashi, 1978') |
                             (df['xtal phases']=='gl+ol+sp')]

# Index all studies not by takahashi,1978 or studies that have gl+ol+sp 
# as xtal phase
not_takahashi = df.loc[(df['Study']!='Takahashi, 1978') |
                       (df['xtal phases']=='gl+ol+sp')]

# Find all studies with NaN in the 'melt CoO' position
no_coo = df_3.loc[df['melt CoO'].isnull()]

# Crosstabulate to get a quick overview of the data in a sheet
cross = pd.crosstab(df['Study'],df['xtal phases'],margins=True)

# You can sum the elements in a series by column
# Total number of studies
cross['All'].sum()
# Total number of studies with xtal phases gl+ol+sp
cross['gl+ol+sp'].sum()

# Sort dataframe alphabetically by Study
sort_df = df.sort_values(['Study'])

# Sort dataframe first by study then by sample #
sort_df = df.sort_values(['Study','sample #'])

# Sort Study ascending, sample decending
# ascending list is boolean 
sort_df = df.sort_values(['Study','sample #'],ascending=[1,0])

#Get values from series as numpy linspace
t_k = df['T(K)'].values

#Merge these two into one dataset
df_merge = pd.concat(df_2[df_2.columns[0:10]],
                     df_3[df_3.columns[9::]],
                     axis=1)

#Save multiple dataframes to different sheets in excel file
writer = pd.ExcelWriter('output.xlsx')
df_merge.to_excel(writer,'Sheet1')
df_2.to_excel(writer,'Sheet2')
df_3.to_excel(writer,'Sheet3')
writer.save()






