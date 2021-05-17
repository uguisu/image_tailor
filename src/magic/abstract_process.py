# coding=utf-8
# author xin.he
import datetime

import cv2
import numpy as np


class AbstractProcess:
    """
    abstract process class
    """

    def __init__(self,
                 width=1754,
                 height=1240):

        assert width is not None
        assert height is not None

        self._width = int(width)
        self._height = int(height)

    def process(self, loop=0):
        """
        process
        :param loop: how many times to loop
        :return: image object as list
        """
        raise RuntimeError('use implement class')

    def get_slice_point(self):
        """
        generate slice point of new image
        :return: a tuple (x, y)
        """
        # refresh seed
        random_generator = np.random.RandomState(datetime.datetime.now().microsecond)

        return (random_generator.randint(10, self._width, size=1)[0],
                random_generator.randint(10, self._height, size=1)[0])

    @staticmethod
    def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
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
