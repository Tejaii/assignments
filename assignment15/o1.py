import numpy as np
import matplotlib.pyplot as plt

# Time array
t = np.linspace(0, 4, 500)

# Generate a triangular waveform using sawtooth from scipy with width=0.5 for symmetry
from scipy.signal import sawtooth
signal = 2.5 * sawtooth(2 * np.pi * (1/2) * t, 0.5) + 2.5  # Scaling to match the voltage levels

# Create the plot
plt.plot(t, signal, color='black')

# Add labels and grid lines
plt.axhline(y=2.5, color='black', linestyle='--', linewidth=0.7)  # 2.5V line
plt.axhline(y=5, color='black', linestyle='--', linewidth=0.7)    # 5V line

# Set plot limits and labels
plt.ylim(0, 6)
plt.xlim(0, 4)
plt.xlabel('t (sec)')
plt.ylabel('(A)')
plt.title('Triangular Waveform')

# Show the plot
plt.show()

