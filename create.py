from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(Path(__file__).parent / "image_matrix_12x20.csv", delimiter=",")

plt.figure(figsize=(12, 6))
plt.imshow(data, cmap="viridis")
plt.colorbar(label="Brightness (0 = black, 255 = white)")

# Print each number inside its cell
for row in range(data.shape[0]):
    for col in range(data.shape[1]):
        plt.text(col, row, int(data[row, col]), ha="center", va="center",
                 color="white", fontsize=7)

plt.title("12x20 brightness matrix of the moon image")
plt.savefig(Path(__file__).parent / "heatmap.png", dpi=150)
plt.show()