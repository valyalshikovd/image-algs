
img = imread('C:\Users\770vd\Downloads\5000-na-5000-pikselei-kartinki-5000x5000px.png'); 

gray_img = rgb2gray(img); 

tic;

sobel_horizontal = fspecial('sobel');
filtered_img_horizontal = imfilter(double(gray_img), sobel_horizontal);

sobel_vertical = sobel_horizontal';
filtered_img_vertical = imfilter(double(gray_img), sobel_vertical);

gradient_magnitude = sqrt(filtered_img_horizontal.^2 + filtered_img_vertical.^2);

elapsed_time = toc;

figure;
subplot(2,2,1); imshow(img); title('Original Image');
subplot(2,2,2); imshow(filtered_img_horizontal, []); title('Sobel Horizontal');
subplot(2,2,3); imshow(filtered_img_vertical, []); title('Sobel Vertical');
subplot(2,2,4); imshow(gradient_magnitude, []); title('Gradient Magnitude');

fprintf('Время выполнения наложения фильтра: %.4f секунд\n', elapsed_time);
