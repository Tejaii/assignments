import numpy as np
import matplotlib.pyplot as plt

# Given midpoint
M = np.array([2, -5])

# Solve for P and Q
# M = (P + Q) / 2
# => 2 * M = P + Q

# Let P = [0, b] and Q = [c, 0]
# Therefore, 2 * M = [0 + c, b + 0] = [c, b]
# So, c = 2 * M[0] and b = 2 * M[1]

c = 2 * M[0]  # 2 * 2 = 4
b = 2 * M[1]  # 2 * (-5) = -10

P = np.array([0, b])  # [0, -10]
Q = np.array([c, 0])  # [4, 0]

# Output the coordinates of P and Q
print(f"Coordinates of P: {P}")
print(f"Coordinates of Q: {Q}")

# Plotting the points and the line segment PQ
plt.figure(figsize=(8, 8))
plt.plot([P[0], Q[0]], [P[1], Q[1]], 'bo-', label='Line PQ')  # Line PQ
plt.scatter(M[0], M[1], color='red', label='Midpoint M (2,-5)')  # Midpoint M
plt.scatter(P[0], P[1], color='green', label=f'Point P (0, {b})')  # Point P
plt.scatter(Q[0], Q[1], color='blue', label=f'Point Q ({c}, 0)')  # Point Q

# Labeling the plot
plt.text(P[0], P[1], 'P', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
plt.text(Q[0], Q[1], 'Q', fontsize=12, verticalalignment='top', horizontalalignment='left')
plt.text(M[0], M[1], 'M', fontsize=12, verticalalignment='top', horizontalalignment='left')

plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.xlim(-1, 5)
plt.ylim(-11, 1)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title('Line Segment PQ with Midpoint M')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()

