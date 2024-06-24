import time
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, filters

img = io.imread('C://Users//770vd//Downloads//5000-na-5000-pikselei-kartinki-5000x5000px.jpg')

gray_img = color.rgb2gray(img)

start_time = time.time()

sobel_horizontal = filters.sobel_h(gray_img)
sobel_vertical = filters.sobel_v(gray_img)

gradient_magnitude = np.sqrt(sobel_horizontal**2 + sobel_vertical**2)

elapsed_time = time.time() - start_time

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
axes[0, 0].imshow(img)
axes[0, 0].set_title('Original Image')
axes[0, 0].axis('off')

axes[0, 1].imshow(sobel_horizontal, cmap='gray')
axes[0, 1].set_title('Sobel Horizontal')
axes[0, 1].axis('off')

axes[1, 0].imshow(sobel_vertical, cmap='gray')
axes[1, 0].set_title('Sobel Vertical')
axes[1, 0].axis('off')

axes[1, 1].imshow(gradient_magnitude, cmap='gray')
axes[1, 1].set_title('Gradient Magnitude')
axes[1, 1].axis('off')

plt.show()

print(f'Время выполнения наложения фильтра: {elapsed_time:.4f} секунд')
