# Importing necessary libraries
import sys  # for path to external scripts
sys.path.insert(0, '/home/teja-vardhan/Desktop/matgeo/codes/CoordGeo')  # path to my scripts
import numpy as np  # Importing numpy
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Local imports
from line.funcs import *
from triangle.funcs import *

# Given points
A = np.array(([2, 2])).reshape(-1, 1)
B = np.array(([-4, -4])).reshape(-1, 1)
C = np.array(([5, -8])).reshape(-1, 1)

# Additional points for median
P = np.array(([2, 2])).reshape(-1, 1)  # Redefining point P (can be same as A)
Q = np.array(([-4, -4])).reshape(-1, 1)  # Redefining point Q (can be same as B)
R = np.array(([5, -8])).reshape(-1, 1)   # Redefining point R (can be same as C)

# Calculating the midpoint of P and Q
M = (P + Q) / 2

# Generating lines for the triangle
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CA = line_gen(C, A)

# Generating line for the median (R to M)
x_RM = line_gen(R, M)

# Plotting the triangle
plt.plot(x_AB[0, :], x_AB[1, :], label='$AB$')
plt.plot(x_BC[0, :], x_BC[1, :], label='$BC$')
plt.plot(x_CA[0, :], x_CA[1, :], label='$CA$')

# Adding the median line to the plot
plt.plot(x_RM[0, :], x_RM[1, :], label='$RM$', linestyle='--')

# Labeling the triangle coordinates
tri_coords = np.block([[A, B, C]])
plt.scatter(tri_coords[0, :], tri_coords[1, :], c='blue')
vert_labels = ['A', 'B', 'C']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt,
                 (tri_coords[0, i], tri_coords[1, i]),
                 textcoords="offset points",
                 xytext=(10, 10),
                 ha='center')

# Adding and labeling point M with coordinates
plt.scatter(M[0, :], M[1, :], c='red')  # Mark point M
plt.annotate(f'M ({M[0,0]:.1f}, {M[1,0]:.1f})',
             (M[0, 0], M[1, 0]),  # Point to label
             textcoords="offset points",
             xytext=(10, 10),  # Distance from text to point
             ha='center')

# Adding and labeling points P, Q, R with coordinates
points = [P, Q, R]
point_labels = ['P', 'Q', 'R']
for i, point in enumerate(points):
    plt.scatter(point[0, :], point[1, :], c='green')  # Mark point P, Q, R
    plt.annotate(f'{point_labels[i]} ({point[0,0]:.1f}, {point[1,0]:.1f})',
                 (point[0, 0], point[1, 0]),
                 textcoords="offset points",
                 xytext=(10, -15),  # Offset text for better readability
                 ha='center')

# Customizing axes
ax = plt.gca()
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.grid()  # Minor grid
plt.axis('equal')

# Show the updated plot with the median and coordinates of points P, Q, R, M
plt.show()

