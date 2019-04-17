import os
import sys
import json
import datetime
import numpy as np
import glob

import skimage.draw,io
from matplotlib import pyplot as plt



print('hello world')
imagePath = 'D:/KerasProject/MaskRCNN/balloon_dataset/balloon/train/53500107_d24b11b3c2_b.jpg'
dirPath = 'D:/KerasProject/MaskRCNN/balloon_dataset/balloon/train/'

myList = glob.glob(r"D:/KerasProject/MaskRCNN/balloon_dataset/balloon/train/*.jpg")



for img in myList:
    # image = skimage.io.imread(img)
    # r = model.detect([image], verbose=1)[0]
    # splash = color_splash(image, r['masks'])
    # file_name = "splash_{:%Y%m%dT%H%M%S}.jpg".format(datetime.datetime.now())
    # fileFinalName = output_path+'/'+file_name
    # skimage.io.imsave(fileFinalName, splash)
    print(img)




#
image = skimage.io.imread(myList[0])
# grayImage = skimage.color.rgb2gray(image)
#
# ImagegrayTrgb = skimage.color.gray2rgb(grayImage)
#
# img_red = np.zeros(list(image.shape), np.uint8)
# img_red[:, :, 0] = np.zeros(list(image.shape)[0:2]) + 255
#
skimage.io.imshow(image)
plt.show()
# #
# # # 创建一张全是0的图像；
# # img = np.zeros([400, 400, 3], np.uint8)
# # skimage.io.imshow(img)
# # plt.show()
# #
# #
# # # 创建一张全是255的图像；
# # img2 = np.ones([300,300,3], np.uint8) * 255
# # skimage.io.imshow(img2)
# # plt.show()
# #
# # # 保存创建的图像；
# #
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
# gray2 = skimage.color.rgb2gray(image)
# skimage.io.imshow(gray2)
# plt.show()

# gray = skimage.color.(skimage.color.rgb2gray(image)) * 255
# skimage.io.imshow(gray)
# plt.show()


# splash = gray.astype(np.uint8)
# file_name = "splash_{:%Y%m%dT%H%M%S}.png".format(datetime.datetime.now())
# skimage.io.imsave(file_name, splash)