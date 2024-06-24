import matplotlib.pyplot as plt
from skimage import io, filters
import numpy as np
import time

image = io.imread('C://Users//770vd//Downloads//5000-na-5000-pikselei-kartinki-5000x5000px.jpg')

start_time = time.time()

red_channel = image[:, :, 0]
green_channel = image[:, :, 1]
blue_channel = image[:, :, 2]

red_blur = filters.gaussian(red_channel, sigma=30)
green_blur = filters.gaussian(green_channel, sigma=30)
blue_blur = filters.gaussian(blue_channel, sigma=30)

gaussian_blur_rgb = np.stack((red_blur, green_blur, blue_blur), axis=-1)

end_time = time.time()
processing_time = end_time - start_time
print(f"Processing time: {processing_time} seconds")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

ax1.imshow(image)
ax1.axis('off')
ax1.set_title('Original Image')

ax2.imshow(gaussian_blur_rgb)
ax2.axis('off')
ax2.set_title('Gaussian Blur (sigma=30)')

plt.show()
