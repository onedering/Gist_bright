# установить библиотеки
# pip install opencv-python
# pip install matplotlib
# изображения должны находиться в одной папке с программой

import cv2
from matplotlib import pyplot as plt

a = ["43.bmp", "43msg100%-LSB.bmp", "43msg50%-LSB.bmp", "43msg10%-LSB.bmp",
     "43msg1%-LSB.bmp"]  # Ввести номера изображений в нужном порядке


def gist(imageN):
    # img = cv2.imread(imageN, 0)
    # histr = cv2.calcHist([img], [0], None, [256], [0, 256])
    # plt.title('Гистограмма ' + a[i])
    # plt.hist(histr, bins=200)
    # # plt.plot(histr, kind='hist')
    # # Автосейв без показа гистограммы
    # # plt.savefig('Гистограмма ' + a[i] + ".jpg")
    # plt.show()
    img = cv2.imread(imageN, cv2.IMREAD_GRAYSCALE)
    plt.title('Гистограмма ' + a[i])
    plt.hist(img.ravel(), 200, [0, 256])
    # plt.savefig('Гистограмма ' + a[i] + ".jpg", edgecolor='b', dpi=300)
    img = 0
    plt.show()



def matrix(imageN):
    img = cv2.imread(imageN)
    # cv2.imshow('image', img)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    value = img_hsv[:, :, 2]
    print("matrix ", a[i])
    print(value)


for i in range(5):
    matrix(a[i])
    gist(a[i])
    i += 1
