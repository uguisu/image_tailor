# coding=utf-8
# author xin.he
from magic import AbstractProcess

import cv2
import datetime
import numpy as np


class JigsawPuzzle(AbstractProcess):
    """
    jigsaw puzzle
    """

    def __init__(self,
                 file_list=None,
                 piece=4,
                 width=1754,
                 height=1240):

        super().__init__(width=width, height=height)

        # verify
        assert file_list is not None
        assert isinstance(file_list, list)
        assert piece is not None
        assert isinstance(piece, int)

        self._file_list = file_list
        self._piece = piece

    def get_image_piece_index(self):
        """
        randomly get image index from input file list
        :return: index as list
        """

        # verify
        if len(self._file_list) < self._piece:
            # do not have enough file to generate target piece
            return [x for x in range(len(self._file_list))]
        # refresh seed
        random_generator = np.random.RandomState(datetime.datetime.now().microsecond)

        rtn = []
        rtn_dict = dict()

        while len(rtn) < self._piece:
            i = random_generator.randint(0, len(self._file_list), size=1)
            if rtn_dict.get(i[0]) is None:
                # avoid duplicate index
                rtn.append(i[0])
                rtn_dict[i[0]] = 1
        return rtn

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

            idx = self.get_image_piece_index()

            (slice_x, slice_y) = self.get_slice_point()
            print(slice_x, slice_y)
            work_img = np.zeros((self._height, self._width, 3), np.uint8)
            work_img = cv2.line(work_img, (0, slice_y), (self._width, slice_y), (0, 255, 0), 2)
            work_img = cv2.line(work_img, (slice_x, 0), (slice_x, self._height), (0, 255, 0), 2)

            for idx_f in idx:
                part_img = cv2.imread(self._file_list[idx_f])
                (h, w) = part_img.shape[:2]

                # debug
                # print(self._file_list[idx_f], 'h = ', h, ', w = ', w)

            cv2.imshow('debug', work_img)
            cv2.waitKey()
