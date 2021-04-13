from skimage import io
from skimage import color
import numpy as np
import matplotlib.pyplot as plt


array = io.imread("example.jpg")
array = color.rgb2gray(array)

grad_x, grad_y = np.gradient(array)

rows = 4
cols = 4

sum_xx = np.cumsum(grad_x, axis=0)
sum_yy = np.cumsum(grad_y, axis=1)
sum_xy = np.cumsum(grad_x, axis=1)
sum_yx = np.cumsum(grad_y, axis=0)

total = sum_xx + sum_yy

print("Min/Max", np.min(array), np.max(array))
print("Diff: ", np.mean(np.abs(array-total)))

normalize = lambda image: (image - np.min(image)) / (np.max(image) - np.min(image))

print("Min/Max input", np.min(normalize(array)), np.max(normalize(array)))
print("Min/Max integral", np.min(normalize(total)), np.max(normalize(total)))
print("Diff: ", np.mean(np.abs(normalize(array)-normalize(total))))


plt.figure(dpi=250)

plt.subplot(rows, cols, 1)
plt.title('sym_xx + sum_yy', loc='center', y = 0.95, fontsize=8)
plt.imshow(array, cmap='gray')
plt.axis('off')
plt.subplot(rows, cols, 2)
plt.imshow(grad_x, cmap='gray') #gradient po x
plt.axis('off')
plt.subplot(rows, cols, 3)
plt.imshow(grad_y, cmap='gray') #gradient po y
plt.axis('off')
plt.subplot(rows, cols, 4)
plt.imshow(total, cmap='gray') #suma skumulowanych sum gradientów po x wzdłóż x i po y wzdłóż y
plt.axis('off')

plt.subplot(rows, cols, 5)
plt.title('vmin = 0 & vmax = 1', loc='center', y = 0.95, fontsize=8)
plt.imshow(array, cmap='gray', vmin=0, vmax=1)
plt.axis('off')
plt.subplot(rows, cols, 6)
plt.imshow(grad_x, cmap='gray') #gradient po x
plt.axis('off')
plt.subplot(rows, cols, 7)
plt.imshow(grad_y, cmap='gray') #gradient po y
plt.axis('off')
plt.subplot(rows, cols, 8)
plt.imshow(total, cmap='gray', vmin=0, vmax=1)
plt.axis('off')     #suma skumulowanych sum gradientów po x wzdłóż x i po y wzdłóż y,
                    # vmin i vmax określają zakres wartości (gdy nie ma wyraźnej normy)

plt.subplot(rows, cols, 9)
plt.title('normalize', loc='center', y = 0.95, fontsize=8)
plt.imshow(normalize(array), cmap='gray', vmin=0, vmax=1)
plt.axis('off')
plt.subplot(rows, cols, 10)
plt.imshow(grad_x, cmap='gray') #gradient po x
plt.axis('off')
plt.subplot(rows, cols, 11)
plt.imshow(grad_y, cmap='gray') #gradient po y
plt.axis('off')
plt.subplot(rows, cols, 12)
plt.imshow(normalize(total), cmap='gray', vmin=0, vmax=1) #znormalizowana sumcumów gradientów
plt.axis('off')

plt.subplot(rows, cols, 13)
plt.title('|norm(array)-norm(total)|', loc='center', y = 0.95, fontsize=8)
plt.imshow(np.abs(normalize(array)-normalize(total)), cmap='gray')
plt.axis('off')
#wartość bezwzględna różnicy znormalizowanego zdjęcia i znormalizowanej sumy cumsumów

plt.show()
