# coding=utf-8
# author xin.he
from share import ImagesLoader

# all files under 'images' will be load
il = ImagesLoader('./images/')
rtn_list = il.file_list
for f in rtn_list:
    print('f1 = ', f)

# to load images under sub-folder
il = ImagesLoader('./images/corgi/')
rtn_list = il.file_list
for f in rtn_list:
    print('f2 = ', f)
