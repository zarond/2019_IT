import matplotlib.pyplot as plt
import numpy as np

img = plt.imread("input.png")[:,:,0:3] # Входное изображение
r = 15                                    # Параметр радиуса
img1 = np.empty_like(img)
img2 = np.empty_like(img)

n = 2 * r + 1
x = np.empty((n,n))
for i in range(n):
    x[i] = (i-r)**2 + (np.arange(n)-r)**2
    
x = np.exp(-x*18/n**2)                  # Охват [-3*sigma,3*sigma]
x/= np.sum(x)

plt.imshow(x, cmap = 'hot')
plt.colorbar()
plt.show()                              # Визуализация ядра свёртки

y = np.empty((n,n,3))                   # Чисто чтобы размерность ядра совпадала
for i in range(n):                      # с размерностью фрагмента изображения
    for j in range(n):                  # Иначе можно отдельно 3 канала считать
        y[i,j] = np.tile(x[i,j],3)      
        
for i in range(r, img.shape[0] - r):  # Свертка 2d
    for j in range(r, img.shape[1] - r):
        img1[i,j] = np.sum(y * img[i-r:i+r+1,j-r:j+r+1,:], axis = (0,1))

ax = plt.subplot(1,2,1)
ax.set_title('2d kernel')
plt.imshow(img1)
        
x = x[r]/np.sum(x[r])             # Ядро 1d

for i in range(r, img.shape[0] - r):  # Свертка 1d по 2м осям
    for j in range(r, img.shape[1] - r):
        img1[i,j] = x.dot(img[i-r:i+r+1,j,:])

for i in range(r, img.shape[0] - r):
    for j in range(r, img.shape[1] - r):
        img2[i,j] = x.dot(img1[i,j-r:j+r+1,:])

ax2 = plt.subplot(1,2,2)
ax2.set_title('1d kernel')
plt.imshow(img2)
plt.show()

