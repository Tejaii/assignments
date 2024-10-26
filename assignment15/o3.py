import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth

# Time array
t = np.linspace(0, 4, 500)

# Generate a triangular waveform with peak values of +5V and -5V
signal = 5 * sawtooth(2 * np.pi * (1/2) * t, 0.5)  # Scale to -5V to +5V

# Create the plot
plt.plot(t, signal, color='black')

# Add labels and grid lines
plt.axhline(y=5, color='black', linestyle='--', linewidth=0.7)  # 5V line
plt.axhline(y=-5, color='black', linestyle='--', linewidth=0.7) # -5V line
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)     # 0V line

# Set plot limits and labels
plt.ylim(-6, 6)
plt.xlim(0, 4)
plt.xlabel('t (sec)')
plt.ylabel('(C)')
plt.title('Triangular Waveform (C)')

# Show the plot
plt.show()

