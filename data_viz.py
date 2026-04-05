import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
temperature = [25, 27, 30, 28, 26]

plt.plot(months, temperature, marker='o', color='green')
plt.title('Average Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.savefig('temperature_plot.png')
plt.show()
