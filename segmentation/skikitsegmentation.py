import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color
from sklearn.cluster import KMeans
import time

image = io.imread('C:/Users/770vd/Downloads/5000-na-5000-pikselei-kartinki-5000x5000px.jpg')
gray_image = color.rgb2gray(image)

pixel_values = gray_image.reshape((-1, 1))
pixel_values = np.float32(pixel_values)

num_clusters = 5

start_time = time.time()

kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(pixel_values)
labels = kmeans.labels_
centers = kmeans.cluster_centers_

elapsed_time = time.time() - start_time
print(f'Время выполнения сегментации: {elapsed_time:.2f} секунд')

labels = labels.flatten()
segmented_image = centers[labels].reshape(gray_image.shape)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Оригинальное изображение')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(segmented_image, cmap='gray')
plt.title('Сегментированное изображение методом k-средних')
plt.axis('off')

plt.show()

plt.figure(figsize=(10, 10))
for i in range(num_clusters):
    masked_image = np.copy(gray_image)
    masked_image = masked_image.reshape((-1, 1))
    masked_image[labels != i] = 0
    masked_image = masked_image.reshape(gray_image.shape)

    plt.subplot(2, 3, i + 1)
    plt.imshow(masked_image, cmap='gray')
    plt.title(f'Регион {i + 1}')
    plt.axis('off')

plt.show()
