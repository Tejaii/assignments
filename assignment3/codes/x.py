#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Rank


import sys                                          #for path to external scripts
sys.path.insert(0, '/home/teja-vardhan/Desktop/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen


#if using termux
import subprocess
import shlex
#end if
data = np.genfromtxt('output.dat', delimiter=' ', names=True)
x = data['P']
y = data['Q']

#Given points
P = np.array(([0,x])).reshape(-1,1)  
Q = np.array(([y,0])).reshape(-1,1)  
M = np.array(([2,-5])).reshape(-1,1) 


#Print rank 
print(LA.matrix_rank(np.block([Q-P,M-P])))

#Generating all lines
x_PQ = line_gen(P,Q)

#Plotting all lines
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')

#Labeling the coordinates
tri_coords = np.block([[P,Q,M]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['P','Q','M']
for i, txt in enumerate(vert_labels):
    #plt.annotate(txt, # this is the text
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.0f}, {tri_coords[1,i]:.0f})',
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# use set_position
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
#plt.xlabel('$x$')
#plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()
