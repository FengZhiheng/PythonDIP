import os
import sys
import json
import datetime
import numpy as np
import skimage.draw

image = skimage.io.imread('D:/KerasProject/Mask_RCNN/balloon_dataset/balloon/train/53500107_d24b11b3c2_b.jpg')
gray = skimage.color.gray2rgb(skimage.color.rgb2gray(image)) * 255
splash = gray.astype(np.uint8)
file_name = "splash_{:%Y%m%dT%H%M%S}.png".format(datetime.datetime.now())
skimage.io.imsave(file_name, splash)