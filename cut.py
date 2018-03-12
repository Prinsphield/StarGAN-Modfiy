# -*- coding:utf-8 -*-
# Created Time: Fri 09 Mar 2018 11:16:26 PM CST
# Author: Taihong Xiao <xiaotaihong@126.com>

import os, cv2
import numpy as np

img = cv2.imread('add_bangs.png')
# for i in range(1,5):
#     cv2.imwrite('smiling_pivot_{}.png'.format(i), img[256*i:256*(i+1), :256, :])

for i in range(1,5):
    img_i = cv2.imread('bangs_pivot_{}_fake.png'.format(i))
    img[256*i:256*(i+1), -256:, :] = img_i[:, 256*1:256*2, :]

cv2.imwrite('bangs.png', img)





