# coding=utf-8
# author xin.he
from magic import SewingMachine
from share import ImagesLoader

import cv2

# create ImagesLoader object
corgi = ImagesLoader('./images/corgi', stander_width=320)
corgi_image_list = corgi.file_list
# sort file list by file name
corgi_image_list.sort()

sewing_machine = SewingMachine(loader=corgi)
rtn = sewing_machine.process()

cv2.imwrite('vertically_stitched_image.jpg', rtn)
