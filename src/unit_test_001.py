# coding=utf-8
# author xin.he
from magic import JigsawPuzzle, StickerPlayer
from share import ImagesLoader


def test_001():
    """
    test ImagesLoader
    """
    il = ImagesLoader('../data')
    rtn_list = il.file_list
    for f in rtn_list:
        print('f = ', f)


def test_020():
    il = ImagesLoader('../data')
    f_list = il.file_list
    jp = JigsawPuzzle(file_list=f_list, piece=4)
    jp.process(loop=1)


def test_030():
    zeng_zhi_shui = ImagesLoader('../data/已切分素材/00001', stander_width=1416, stander_height=826)
    huo_che_piao = ImagesLoader('../data/已切分素材/00002', stander_width=508, stander_height=319)

    loader_list = [zeng_zhi_shui, huo_che_piao]

    sp = StickerPlayer(loader_list=loader_list, piece=3)
    sp.process(loop=1)


if __name__ == '__main__':
    test_001()
    # test_020()
    # test_030()
