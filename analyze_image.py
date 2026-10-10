from pathlib import Path

import cv2
import numpy as np

# ---------- 1. Load the image ----------
IMAGE_PATH = Path(__file__).parent / "sample_image.jpeg"
img = cv2.imread(str(IMAGE_PATH))
if img is None:
    raise SystemExit(f"Could not load image: {IMAGE_PATH}")

print("Image shape (rows, columns, channels):", img.shape)

# ---------- 2. The image AS A MATRIX of numbers ----------
# numpy shortens huge arrays with "..." so the console isn't flooded.
# What you see IS the real matrix; the "..." just hides the middle part.
print("\nCOLOR MATRIX (each pixel = [Blue Green Red]):")
print(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("\nGRAYSCALE MATRIX (each pixel = one number, 0=black, 255=white):")
print(gray)

# ---------- 3. A complete, readable matrix: shrink the image to 12x20 ----------
# Printing 14 million numbers is impossible, so we shrink the image
# until the WHOLE matrix fits on screen.
tiny = cv2.resize(gray, (20, 12), interpolation=cv2.INTER_AREA)
np.set_printoptions(linewidth=200)
print("\nWHOLE IMAGE shrunk to 12 rows x 20 columns (full matrix, nothing hidden):")
print(tiny)

# ---------- 4. A spot of the ORIGINAL image (your assignment's 'spot') ----------
ROW, COL = 953, 2560  # roughly the center of the moon

print(f"\n10x10 grayscale spot at row={ROW}, col={COL}:")
print(gray[ROW:ROW + 10, COL:COL + 10])

print(f"\n3x3 color spot at row={ROW}, col={COL} ([B G R] per pixel):")
print(img[ROW:ROW + 3, COL:COL + 3])

b, g, r = img[ROW, COL]
print(f"\nSingle pixel at ({ROW}, {COL}): Blue={b}, Green={g}, Red={r}")

# ---------- 5. Save the small matrix to a file ----------
out_file = Path(__file__).parent / "image_matrix_12x20.csv"
np.savetxt(out_file, tiny, fmt="%d", delimiter=",")
print(f"\nSaved the 12x20 matrix to: {out_file.name}")