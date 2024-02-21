import matplotlib.pyplot as plt
import numpy as np

# Assuming nut_butter_prices and graphs_dir are already defined as before
nut_butter_prices = {"Almond butter": 10, "Peanut butter": 8, "Cashew butter": 12}
graphs_dir = "./graphs"

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
(ax1, ax2), (ax3, ax4) = axs  # Unpack the axes for easy reference

x = np.array([1, 2, 3, 4])

# Plot data to each axis
ax1.plot(x, np.divide(x, 2))
ax2.scatter(np.random.random(10), np.random.random(10))
ax3.bar(nut_butter_prices.keys(), nut_butter_prices.values())
ax4.hist(np.random.randn(1000))

plt.tight_layout()  # Adjust the layout
fig.savefig(f"{graphs_dir}/multiplot.png")

# Clear the axes if you plan to reuse them, but since we're saving immediately after plotting, this might be unnecessary unless you're adding more plots later
ax1.clear()
ax2.clear()
ax3.clear()
ax4.clear()

# If you're creating a new figure or want to reuse the figure for different plots, consider redefining fig and axs as needed.
axs[0, 0].plot(x, np.divide(x, 2))
axs[0, 1].scatter(np.random.random(10), np.random.random(10))
axs[1, 0].bar(nut_butter_prices.keys(), nut_butter_prices.values())
axs[1, 1].hist(np.random.randn(1000))

plt.tight_layout()  # Adjust the layout for clarity and to prevent overlap
fig.savefig(f"{graphs_dir}/multiplot1.png")

# If you wish to clear the plots after saving to start fresh, you can loop through axs
for ax in axs.flat:
    ax.clear()