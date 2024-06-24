import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from PIL import Image
import time

image_path = 'C://Users//770vd//Downloads//5000-na-5000-pikselei-kartinki-5000x5000px.jpg'
image = np.array(Image.open(image_path).convert('RGB'))

if len(image.shape) < 3 or image.shape[2] != 3:
    raise ValueError("Изображение не имеет трех каналов RGB.")

sigma = 10

start_time = time.time()

filtered_image = np.zeros_like(image)
for channel in range(3):
    filtered_image[:, :, channel] = gaussian_filter(image[:, :, channel], sigma=sigma)

elapsed_time = time.time() - start_time
print(f"Время выполнения фильтрации Гаусса: {elapsed_time:.4f} секунд")

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Исходное изображение')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(filtered_image)
plt.title(f'Отфильтрованное изображение (σ = {sigma})')
plt.axis('off')

plt.tight_layout()
plt.show()
