import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os

# Load the C library
lib = ctypes.CDLL('./problem1_c_code.so')  # Ensure this path points to your compiled C library

# Define function signature for the C function
lib.compute_points.argtypes = [
    ctypes.POINTER(ctypes.c_double),  # x_values array
    ctypes.POINTER(ctypes.c_double),  # y_values array
    ctypes.c_int,                     # num_points
    ctypes.c_double                   # h (step size)
]

# Parameters
num_points = 100
h = 0.01

# Arrays to store computed points (blue)
x_values = (ctypes.c_double * num_points)()
y_values = (ctypes.c_double * num_points)()

# Call the C function
lib.compute_points(x_values, y_values, num_points, h)

# Convert results to Python lists for plotting
x_values = np.array(list(x_values))
y_values = np.array(list(y_values))

# Exact function (red curve)
x_exact = np.linspace(0, 2, 100)
y_exact = np.log(np.exp(x_exact) + np.exp(-x_exact))

# Plot the exact function
plt.plot(x_exact, y_exact, label=r"Exact: $f(x) = \ln(e^x + e^{-x})$", color="red")

# Plot the computed points (blue)
plt.scatter(x_values, y_values, color="blue", label="Computed Points", s=10)

# Finalize plot
plt.grid(True)
plt.legend()
plt.title("Comparison of Exact and Computed Solutions")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(0, 2)
plt.ylim(0, 2)
plt.show()
