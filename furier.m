
img = imread('C:\Users\770vd\Downloads\5000-na-5000-pikselei-kartinki-5000x5000px.png');


if size(img, 3) == 3
    img = rgb2gray(img);
end

figure;
imshow(img);
title('Исходное изображение');

tic;

F = fft2(double(img));

Fsh = fftshift(F);
execution_time = toc;

amplitude_spectrum = log(1 + abs(Fsh));

figure;
imshow(amplitude_spectrum, []);
title('Амплитудный спектр');

phase_spectrum = angle(Fsh);

figure;
imshow(phase_spectrum, []);
title('Фазовый спектр');

fprintf('Время выполнения преобразования Фурье: %.6f секунд\n', execution_time);
