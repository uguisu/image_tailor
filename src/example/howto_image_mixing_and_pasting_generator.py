# coding=utf-8
# author xin.he
from magic import StickerPlayer
from share import ImagesLoader

# create ImagesLoader object
fee_receipt = ImagesLoader('./images/supermarket_fee_receipt', stander_width=175)
corgi = ImagesLoader('./images/corgi', stander_width=640, stander_height=480)
# push ImagesLoader objects into a list
loader_list = [fee_receipt, corgi]

# call StickerPlayer to generate
sp = StickerPlayer(loader_list=loader_list,
                   piece=3,
                   width=1024,
                   height=768)
sp.process(loop=1)
