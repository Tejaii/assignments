import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth

# Time array
t = np.linspace(0, 4, 500)

# Generate a triangular waveform using sawtooth with width=0.5 for symmetry
signal = 2.5 * sawtooth(2 * np.pi * (1/2) * t, 0.5) - 2.5  # Shift and scale to -5V to 0V

# Create the plot
plt.plot(t, signal, color='black')

# Add labels and grid lines
plt.axhline(y=-2.5, color='black', linestyle='--', linewidth=0.7)  # -2.5V line
plt.axhline(y=-5, color='black', linestyle='--', linewidth=0.7)    # -5V line
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)        # 0V line

# Set plot limits and labels
plt.ylim(-6, 1)
plt.xlim(0, 4)
plt.xlabel('t (sec)')
plt.ylabel('(B)')
plt.title('Triangular Waveform (B)')

# Show the plot
plt.show()

