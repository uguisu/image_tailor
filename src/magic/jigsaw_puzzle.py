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
                 weight=1920,
                 height=1080):
        super().__init__()

        # verify
        assert file_list is not None
        assert isinstance(file_list, list)
        assert piece is not None
        assert isinstance(piece, int)
        assert weight is not None
        assert height is not None

        self._file_list = file_list
        self._piece = piece
        self._weight = int(weight)
        self._height = int(height)

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

            for idx_f in idx:
                part_img = cv2.imread(self._file_list[idx_f])
                (h, w) = part_img.shape[:2]

                # debug
                # print(self._file_list[idx_f], 'h = ', h, ', w = ', w)
