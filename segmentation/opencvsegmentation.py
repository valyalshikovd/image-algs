import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

image = cv2.imread('C:/Users/770vd/Downloads/5000-na-5000-pikselei-kartinki-5000x5000px.jpg', cv2.IMREAD_GRAYSCALE)

pixel_values = image.reshape((-1, 1))
pixel_values = np.float32(pixel_values)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
num_clusters = 5

start_time = time.time()

_, labels, centers = cv2.kmeans(pixel_values, num_clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

elapsed_time = time.time() - start_time
print(f'Время выполнения сегментации: {elapsed_time:.2f} секунд')

labels = labels.flatten()
segmented_image = centers[labels].reshape(image.shape).astype(np.uint8)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Оригинальное изображение')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(segmented_image, cmap='gray')
plt.title('Сегментированное изображение методом k-средних')
plt.axis('off')

plt.show()

plt.figure(figsize=(10, 10))
for i in range(num_clusters):
    masked_image = np.copy(image)
    masked_image = masked_image.reshape((-1, 1))
    masked_image[labels != i] = 0
    masked_image = masked_image.reshape(image.shape)

    plt.subplot(2, 3, i + 1)
    plt.imshow(masked_image, cmap='gray')
    plt.title(f'Регион {i + 1}')
    plt.axis('off')

plt.show()
