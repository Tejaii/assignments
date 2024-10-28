import matplotlib.pyplot as plt
import numpy as np

# Define the time points and flux values
t = [0, 1, 2, 2.5]
phi = [0, 0.12, 0.12, 0]

# Create the plot
plt.figure(figsize=(8, 4))
plt.plot(t, phi, 'b-', linewidth=2)

# Add labels and title
plt.xlabel('t (s)', fontsize=14)
plt.ylabel('Φ (Wb)', fontsize=14)
plt.title('Flux vs Time', fontsize=16)

# Set axis limits
plt.xlim(-0.2, 3)
plt.ylim(-0.02, 0.14)

# Add grid lines
plt.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
