
image = imread('C:\Users\770vd\Downloads\5000-na-5000-pikselei-kartinki-5000x5000px.png');

sigma = 10; 
tic;
filtered_image = imgaussfilt(image, sigma);

elapsed_time = toc;

fprintf('Время выполнения фильтрации Гаусса: %.4f секунд\n', elapsed_time);

subplot(1, 2, 1);
imshow(image);
title('Исходное изображение');

subplot(1, 2, 2);
imshow(filtered_image);
title('Отфильтрованное изображение');
