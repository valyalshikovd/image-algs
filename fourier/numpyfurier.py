import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft2, fftshift
from skimage import io, color
import time

img = io.imread('C://Users//770vd//Downloads//5000-na-5000-pikselei-kartinki-5000x5000px.jpg')

if len(img.shape) == 3:
    img = color.rgb2gray(img)

plt.figure()
plt.imshow(img, cmap='gray')
plt.title('Исходное изображение')
plt.axis('off')

start_time = time.time()


F = fft2(img)


Fsh = fftshift(F)

execution_time = time.time() - start_time


amplitude_spectrum = np.log(1 + np.abs(Fsh))


plt.figure()
plt.imshow(amplitude_spectrum, cmap='gray')
plt.title('Амплитудный спектр')
plt.axis('off')

phase_spectrum = np.angle(Fsh)

plt.figure()
plt.imshow(phase_spectrum, cmap='gray')
plt.title('Фазовый спектр')
plt.axis('off')

print(f'Время выполнения преобразования Фурье: {execution_time:.6f} секунд')

plt.show()
