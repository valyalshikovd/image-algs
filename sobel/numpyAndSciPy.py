import time

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from skimage import io, color

img = io.imread('C://Users//770vd//Downloads//5000-na-5000-pikselei-kartinki-5000x5000px.jpg')

start_time = time.time()
gray_img = color.rgb2gray(img)

sobel_horizontal = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_vertical = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

filtered_img_horizontal = ndimage.convolve(gray_img, sobel_horizontal)
filtered_img_vertical = ndimage.convolve(gray_img, sobel_vertical)

gradient_magnitude = np.sqrt(filtered_img_horizontal**2 + filtered_img_vertical**2)

end_time = time.time()
processing_time = end_time - start_time
print(f"Processing time: {processing_time} seconds")

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
axes[0, 0].imshow(img, cmap='gray')
axes[0, 0].set_title('Original Image')
axes[0, 0].axis('off')

axes[0, 1].imshow(filtered_img_horizontal, cmap='gray')
axes[0, 1].set_title('Sobel Horizontal')
axes[0, 1].axis('off')

axes[1, 0].imshow(filtered_img_vertical, cmap='gray')
axes[1, 0].set_title('Sobel Vertical')
axes[1, 0].axis('off')

axes[1, 1].imshow(gradient_magnitude, cmap='gray')
axes[1, 1].set_title('Gradient Magnitude')
axes[1, 1].axis('off')

plt.show()

