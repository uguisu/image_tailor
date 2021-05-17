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
                rtn = self.resize(rtn, width=self._loader.stander_width)

                continue
            else:
                wrk_rtn = cv2.imread(wrk_img)
                wrk_rtn = self.resize(wrk_rtn, width=self._loader.stander_width)

                rtn = cv2.vconcat([rtn, wrk_rtn])

        return rtn
