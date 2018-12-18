import cv2
import numpy as np
from matplotlib import pyplot as plt
from glob import glob
from random import randint
import random

data = glob("imgs/*.jpg")

count = 0

# random.shuffle(data)

for imname in data:

    cimg = cv2.imread(imname,1)
    source = cimg
    source = cv2.resize(source, (256,256))

    cimg = np.fliplr(cimg.reshape(-1,3)).reshape(cimg.shape)
    cimg = cv2.resize(cimg, (256,256))

    img = cv2.imread(imname,0)
    
    for i in range(30):
        randx = randint(0,205)
        randy = randint(0,205)
        cimg[randx:randx+50, randy:randy+50] = 255
    blur = cv2.blur(cimg,(100,100))

    img_edge = cv2.adaptiveThreshold(img, 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY,
                                    blockSize=9,
                                    C=2)
    img_edge = cv2.resize(img_edge, (256,256))

    gray_img = cv2.merge([img_edge,img_edge,img_edge])

    concat_img = np.concatenate((source,gray_img),axis=1)

    count = count + 1

    print(count)

    if (count > 2000) & (count < 4000):
        cv2.imwrite('./datasets/comic/val/' + imname[5:],concat_img)
    elif (count > 4000) & (count < 6000):
        cv2.imwrite('./datasets/comic/test/' + imname[5:],concat_img)
    elif count > 6000:
        cv2.imwrite('./datasets/comic/train/' + imname[5:],concat_img)
    else:
        cv2.imwrite('./datasets/comic/minitrain/' + imname[5:],concat_img)