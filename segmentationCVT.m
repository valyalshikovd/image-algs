% Загрузка цветного изображения
RGB = imread('C:\Users\770vd\Downloads\5000-na-5000-pikselei-kartinki-5000x5000px.jpg');

% Преобразование в черно-белое изображение
I = rgb2gray(RGB);

% Преобразование изображения в одномерный массив
data = double(I(:));

% Измерение времени начала сегментации
tic;

% Количество кластеров
K = 5;

% Запуск алгоритма k-средних
[idx, centroids] = kmeans(data, K);

% Измерение времени окончания сегментации и вычисление времени выполнения
segmentation_time = toc;

% Восстановление изображения
segmented_image = reshape(centroids(idx), size(I));

% Отображение результатов
figure;

% Оригинальное черно-белое изображение
subplot(2, 3, 1);
imshow(I);
title('Исходное черно-белое изображение');

% Сегментированное изображение
subplot(2, 3, 2);
imshow(segmented_image, []);
title('Сегментированное изображение методом k-средних');
fprintf('Время сегментирования: %.2f секунд\n', segmentation_time);
% Отображение каждого кластера отдельно
for k = 1:K
    cluster_image = zeros(size(I));
    cluster_image(idx == k) = centroids(k);
    subplot(2, 3, 2 + k);
    imshow(cluster_image, []);
    title(sprintf('Кластер %d', k));
end

% Вывод времени выполнения


