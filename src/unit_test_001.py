# coding=utf-8
# author xin.he
from share import ImagesLoader


def test_001():
    """
    test ImagesLoader
    """
    il = ImagesLoader('../data')
    rtn_list = il.load_file_list()
    for f in rtn_list:
        print('f = ', f)


if __name__ == '__main__':
    test_001()
