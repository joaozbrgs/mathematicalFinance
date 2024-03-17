import matplotlib.pyplot as plt
import numpy as np
import handyFinance as hf

# Assuming the user inputs the principal amount (C), interest rate (i), and number of periods (n)
C = float(input("Enter the principal amount (C): "))
i = float(input("Enter the interest rate per period (i): "))
n = int(input("Enter the number of periods (n): "))

# Calculate the simple interest for each period
M_values = [C * (1 + i * period) for period in range(n+1)]

# Generate the x-axis values (time periods)
time_periods = np.arange(0, n+1, 1)

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(time_periods, M_values, marker='o')

# Labeling the axes and title
plt.title('Simple Interest Growth Over Time')
plt.xlabel('Number of Periods (n)')
plt.ylabel('Future Value (M)')

# Display the grid and the plot
plt.grid(True)
plt.show()