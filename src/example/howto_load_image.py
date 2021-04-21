# coding=utf-8
# author xin.he
from share import ImagesLoader

il = ImagesLoader('./images/')
rtn_list = il.load_file_list()
for f in rtn_list:
    print('f = ', f)
