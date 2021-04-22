# coding=utf-8
# author xin.he
from magic import AbstractProcess

import cv2
import datetime
import numpy as np

from share import ImagesLoader


class StickerPlayer(AbstractProcess):
    """
    sticker player
    """

    def __init__(self,
                 loader_list=None,
                 piece=4,
                 width=1754,
                 height=1240,
                 border=10):

        super().__init__(width=width, height=height)

        # verify
        assert loader_list is not None and isinstance(loader_list, list)
        assert piece is not None and isinstance(piece, int)
        assert border is not None and isinstance(border, int)

        self._loader_list = loader_list
        self._piece = piece
        self._border = border
        # refresh seed
        self._random_generator = np.random.RandomState(datetime.datetime.now().microsecond)

    def get_slice_image(self):
        """
        randomly pickup a image and zoom to target size
        :return: resized image
        """
        # pick a loader
        loader_idx = 0
        if 1 < len(self._loader_list):
            loader_idx = self._random_generator.randint(0, len(self._loader_list), size=1)
        _loader = self._loader_list[loader_idx[0]]

        # check type
        assert isinstance(_loader, ImagesLoader)

        # pick a image
        sticker_idx = self._random_generator.randint(0, len(_loader.file_list), size=1)
        part_img = cv2.imread(_loader.file_list[sticker_idx[0]])
        # (ori_h, ori_w) = part_img.shape[:2]

        # zoom
        part_img = self._resize(part_img, _loader.stander_width, _loader.stander_height)
        return part_img

    def _resize(self, image, width=None, height=None, inter=cv2.INTER_AREA):
        """
        resize
        copy from imutils.convenience
        """

        dim = None
        (ori_h, ori_w) = image.shape[:2]

        if width is not None:
            r = width / float(ori_w)
            dim = (width, int(ori_h * r))
        else:
            r = height / float(ori_h)
            dim = (int(ori_w * r), height)

        _im = cv2.resize(image, dim, interpolation=inter)

        return _im

    def process(self, loop=0):
        """
        process
        :param loop: how many times to loop
        :return: image object as list
        """
        # verify
        assert loop is not None
        assert isinstance(loop, int)
        assert loop >= 0

        if 0 == loop:
            return None

        for i in range(loop):

            # create a new blank image
            blank_image = np.ones((self._height, self._width, 3), dtype="uint8") * 180

            pin = {
                "h": self._border,
                "w": self._border
            }
            max_width = 0

            for j in range(self._piece):
                # get a sticker index
                _sticker = self.get_slice_image()
                (sticker_h, sticker_w) = _sticker.shape[:2]

                # TODO debug
                print('sticker_h = ', sticker_h, ', sticker_w = ', sticker_w)

                # size check
                if pin["h"] + sticker_h > self._height:
                    # move pin location
                    pin["h"] = self._border
                    pin["w"] = max_width
                    # TODO debug
                    print('size check, change pin to = ', pin)

                if pin["h"] + sticker_h > self._height or pin["w"] + sticker_w > self._width:
                    # image too big, skip it
                    continue

                blank_image[pin["h"]:pin["h"] + sticker_h, pin["w"]:pin["w"] + sticker_w] = _sticker

                pin["h"] = pin["h"] + sticker_h + self._border
                max_width = max(max_width, pin["w"] + sticker_w)

                # TODO debug
                print('pin = ', pin)
                print('max_width = ', max_width)

            # TODO debug
            # cv2.imshow('fixed', blank_image)
            # cv2.waitKey()
            cv2.imwrite('debug.jpg', blank_image)
