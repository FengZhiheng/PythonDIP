import os
import sys
import json
import datetime
import numpy as np

import skimage.draw,io
from matplotlib import pyplot as plt



print('hello world')
image = skimage.io.imread('D:/KerasProject/Mask_RCNN/balloon_dataset/balloon/train/53500107_d24b11b3c2_b.jpg')
skimage.io.imshow(image)
plt.show()
#
# # 创建一张全是0的图像；
# img = np.zeros([400, 400, 3], np.uint8)
# skimage.io.imshow(img)
# plt.show()
#
#
# # 创建一张全是255的图像；
# img2 = np.ones([300,300,3], np.uint8) * 255
# skimage.io.imshow(img2)
# plt.show()
#
# # 保存创建的图像；
#
#
#
# # 对3通道的图像进行灰度化
#
# plt.show()
# skimage.io.imsave('D:/PythonProject/PathonDIP/aaa.jpg', image)
#
#
#
# a = np.array([2,4,6,8,10])
# b = np.where(a > 5)
# print(b)
#
#
#
#
#
gray2 = skimage.color.rgb2gray(image)
skimage.io.imshow(gray2)
plt.show()

gray = skimage.color.(skimage.color.rgb2gray(image)) * 255
skimage.io.imshow(gray)
plt.show()


# splash = gray.astype(np.uint8)
# file_name = "splash_{:%Y%m%dT%H%M%S}.png".format(datetime.datetime.now())
# skimage.io.imsave(file_name, splash)