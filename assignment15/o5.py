import matplotlib.pyplot as plt

# Define the time intervals
t1 = [0, 1]
t2 = [2, 2.5]

# Define the voltage values
v1 = [24, 24]
v2 = [-48, -48]

# Plot the graph
plt.plot(t1, v1, 'r-', linewidth=2)
plt.plot(t2, v2, 'k-', linewidth=2)

# Set the axis labels and title
plt.xlabel('t(s)')
plt.ylabel('Cm')
plt.title('Voltage vs Time')

# Set the axis limits
plt.xlim(-0.5, 3)
plt.ylim(-55, 30)

# Add the grid
plt.grid(True)

# Show the plot
plt.show()
