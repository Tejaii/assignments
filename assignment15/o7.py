import matplotlib.pyplot as plt

# Define the time points and corresponding voltage values for the new graph
t_new = [0, 1, 2, 2.5]
voltage_new = [-24, 0, 48, 0]

# Plot the new graph
plt.step(t_new, voltage_new, where='post')

# Labels and title
plt.xlabel('t(s)')
plt.ylabel('eₐₛ (V)')
plt.title('Voltage vs Time (New)')

# Set the voltage limits
plt.ylim(-30, 50)

# Display the plot
plt.grid(True)
plt.show()

