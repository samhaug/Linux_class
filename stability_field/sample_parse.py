'''
==============================================================================

File Name : sample_parse.py
Purpose : Learn to parse file
Creation Date : 11-01-2018
Last Modified : Thu 11 Jan 2018 12:54:28 PM EST
Created By : Samuel M. Haugland

___________.__                                                         _____
\__    ___/|  |__   ____   ______   ______  _  __ ___________    _____/ ____\
  |    |   |  |  \_/ __ \  \____ \ /  _ \ \/ \/ // __ \_  __ \  /  _ \   __\
  |    |   |   Y  \  ___/  |  |_> >  <_> )     /\  ___/|  | \/ (  <_> )  |
  |____|   |___|  /\___  > |   __/ \____/ \/\_/  \___  >__|     \____/|__|
                \/     \/  |__|                      \/
             __________          __  .__
             \______   \___.__._/  |_|  |__   ____   ____
              |     ___<   |  |\   __\  |  \ /  _ \ /    \
              |    |    \___  | |  | |   Y  (  <_> )   |  \
              |____|    / ____| |__| |___|  /\____/|___|  /
                        \/                \/            \/

==============================================================================
'''

#open scorodite.txt in read mode.
f = open('scorodite.txt','r')

lines = f.readlines()

#Strip each line of leading and trailing whitespace and newline 
#characters and then split each element by whitespace.

a = []
for ii in lines:
    a.append(ii.strip().split())

#Use list comprehension to achieve the same thing in one line
#Google 'list comprehension'

a = [ii.strip().split() for ii in lines]

# Find what index of a has the list ['Main', 'Diagram']
ind = a.index(['Main', 'Diagram'])

# Now only consider that list from this index+4 to the end

a = a[ind+4::]

#Now find the indices that start with a letter.

alpha_index = []
for idx,ii in enumerate(a):
    if ii[0][0].isalpha():
        alpha_index.append(idx)







