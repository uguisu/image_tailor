# coding=utf-8
# author xin.he
import cv2

from magic import AbstractProcess
from share import ImagesLoader


class SewingMachine(AbstractProcess):
    """
    Sewing Machine
    vertically stitch image

    SewingMachine will read ImagesLoader's `stander_width` property and automatically resize all images to
    fit `stander_width`
    """

    def __init__(self,
                 loader=None):
        super().__init__(width=0, height=0)

        # verify
        assert loader is not None
        assert isinstance(loader, ImagesLoader)

        self._loader = loader

    def process(self, loop=0):
        """
        process
        :param loop: how many times to loop
        """

        file_list = self._loader.file_list
        file_list.sort()

        rtn = None
        for wrk_img in file_list:
            if rtn is None:
                rtn = cv2.imread(wrk_img)
                rtn = self._resize(rtn, width=self._loader.stander_width)

                continue
            else:
                wrk_rtn = cv2.imread(wrk_img)
                wrk_rtn = self._resize(wrk_rtn, width=self._loader.stander_width)

                rtn = cv2.vconcat([rtn, wrk_rtn])

        return rtn

    def _resize(self, image, width=None, height=None, inter=cv2.INTER_AREA):
        """
        resize
        copy from imutils.convenience
        TODO move to share
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
