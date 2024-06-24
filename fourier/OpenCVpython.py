import cv2
import numpy as np
import matplotlib.pyplot as plt
import time


img = cv2.imread('C://Users//770vd//Downloads//5000-na-5000-pikselei-kartinki-5000x5000px.jpg', cv2.IMREAD_GRAYSCALE)

plt.figure()
plt.imshow(img, cmap='gray')
plt.title('Исходное изображение')
plt.axis('off')

start_time = time.time()

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

dft_shift = np.fft.fftshift(dft)

execution_time = time.time() - start_time

magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

plt.figure()
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Амплитудный спектр')
plt.axis('off')

phase_spectrum = np.angle(dft_shift[:, :, 0] + 1j * dft_shift[:, :, 1])

plt.figure()
plt.imshow(phase_spectrum, cmap='gray')
plt.title('Фазовый спектр')
plt.axis('off')

print(f'Время выполнения преобразования Фурье: {execution_time:.6f} секунд')

plt.show()
