import cv2
import numpy as np
import time

# Загрузка изображения
image = cv2.imread('C://Users//770vd//Downloads//5000-na-5000-pikselei-kartinki-5000x5000px.jpg')

# Запуск отсчета времени
start_time = time.time()

gaussian_blur = cv2.GaussianBlur(image, (31, 31), 10)

end_time = time.time()
processing_time = end_time - start_time
print(f"Processing time: {processing_time} seconds")

cv2.imshow('Original Image', image)
cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
