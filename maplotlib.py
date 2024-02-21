import matplotlib.pyplot as plt
import numpy as np

# Ensure the directory exists
import os
graphs_dir = "./graphs"
if not os.path.exists(graphs_dir):
    os.makedirs(graphs_dir)

# Simple Plot
x = np.array([1, 2, 3, 4])  # Use numpy array for easy operations
y = np.array([11, 22, 33, 44])

fig, ax = plt.subplots(figsize=(5, 5))
ax.plot(x, y)
ax.set(title="Sample Simple Plot", xlabel="x-axis", ylabel="y-axis")
fig.savefig(f"{graphs_dir}/simple-plot.png")

# Line Plotting
fig, ax = plt.subplots(figsize=(5, 5))
ax.plot(x, x**2)  # Now x is a numpy array, so this operation is valid
fig.savefig(f"{graphs_dir}/line-plot.png")

# Scatter Plotting
fig, ax = plt.subplots(figsize=(5, 5))
ax.scatter(x, np.exp(x))
fig.savefig(f"{graphs_dir}/scatter-plot.png")

ax.clear()  # Clear the axis for a new plot
ax.scatter(x, np.sin(x))
fig.savefig(f"{graphs_dir}/scatter-plot2.png")
ax.clear()  # Clear the axis for a new plot

# Bar Plotting
nut_butter_prices = {"Almond butter": 10,
                     "Peanut butter": 8, "Cashew butter": 12}
fig, ax = plt.subplots(figsize=(5, 5))
ax.bar(nut_butter_prices.keys(), nut_butter_prices.values())
ax.set(title="Dan's Nut Butter Store", ylabel="Price ($)")
fig.savefig(f"{graphs_dir}/bar-plot.png")
ax.clear()  # Clear the axis for a new plot

# For horizontal bar plot, create a new figure
fig, ax = plt.subplots(figsize=(5, 5))
ax.barh(list(nut_butter_prices.keys()), list(nut_butter_prices.values()))
plt.tight_layout()
fig.savefig(f"{graphs_dir}/bar-plot1.png")
ax.clear()  # Clear the axis for a new plot

# Histogram
x = np.random.randn(1000)  # pulls data from a normal distribution
fig, ax = plt.subplots(figsize=(5, 5))
ax.hist(x)
fig.savefig(f"{graphs_dir}/histogram-plot.png")
ax.clear()  # Clear the axis for a new plot
