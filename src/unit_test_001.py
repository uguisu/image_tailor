# coding=utf-8
# author xin.he
from magic import JigsawPuzzle
from share import ImagesLoader


def test_001():
    """
    test ImagesLoader
    """
    il = ImagesLoader('../data')
    rtn_list = il.load_file_list()
    for f in rtn_list:
        print('f = ', f)


def test_002():
    il = ImagesLoader('../data')
    f_list = il.load_file_list()
    jp = JigsawPuzzle(file_list=f_list, piece=4)
    jp.process(loop=1)


if __name__ == '__main__':
    test_001()
    test_002()
