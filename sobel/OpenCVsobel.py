import cv2
import numpy as np
import time
import matplotlib.pyplot as plt


img = cv2.imread('C://Users//770vd//Downloads//5000-na-5000-pikselei-kartinki-5000x5000px.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

start_time = time.time()

sobel_horizontal = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=5)
sobel_vertical = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=5)

gradient_magnitude = cv2.magnitude(sobel_horizontal, sobel_vertical)

elapsed_time = time.time() - start_time

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
axes[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
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
