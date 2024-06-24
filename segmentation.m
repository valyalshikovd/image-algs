
RGB = imread('C:\Users\770vd\Downloads\5000-na-5000-pikselei-kartinki-5000x5000px.jpg');

I = rgb2gray(RGB);

tic;

K = 5;

pixel_labels = imsegkmeans(I, K);

segmentation_time = toc;

segmented_image = zeros(size(I));
for k = 1:K
    segmented_image(pixel_labels == k) = mean(I(pixel_labels == k), 'all');
end

figure;

subplot(2, 3, 1);
imshow(I);
title('Исходное черно-белое изображение');

subplot(2, 3, 2);
imshow(segmented_image, []);
title('Сегментированное изображение методом k-средних (imsegkmeans)');
fprintf('Время сегментирования: %.2f секунд\n', segmentation_time);
for k = 1:K
    cluster_image = zeros(size(I));
    cluster_image(pixel_labels == k) = mean(I(pixel_labels == k), 'all');
    subplot(2, 3, 2 + k);
    imshow(cluster_image, []);
    title(sprintf('Кластер %d', k));
end



