import matplotlib.pyplot as plt
import numpy as np

# Define the time intervals and voltage values
t1 = np.linspace(0, 1, 100)
v1 = 24 * np.ones(100)

t2 = np.linspace(1, 2, 100)
v2 = np.zeros(100)

t3 = np.linspace(2, 2.5, 50)
v3 = 48 * np.ones(50)

# Combine the time and voltage arrays
t = np.concatenate([t1, t2, t3])
v = np.concatenate([v1, v2, v3])

# Plot the graph
plt.plot(t, v, 'b-', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Voltage vs Time')
plt.grid(True)
plt.show()
