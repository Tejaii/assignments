import matplotlib.pyplot as plt
import numpy as np

# Define the time range
t = np.linspace(0, 3, 100)

# Define the voltage function
def voltage(t):
    if t < 1:
        return -24
    elif t < 2:
        return 0
    elif t < 2.5:
        return 48
    else:
        return 0

# Calculate the voltage values
v = [voltage(t_i) for t_i in t]

# Create the plot
plt.figure(figsize=(8, 4))
plt.plot(t, v, linewidth=2)

# Set labels and grid
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid(True)

# Set axis limits
plt.ylim(-30, 50)

# Add dashed lines for voltage levels
plt.axhline(y=48, color='gray', linestyle='--')
plt.axhline(y=-24, color='gray', linestyle='--')

# Show the plot
plt.show()
