# coding=utf-8
# author xin.he
import datetime
import numpy as np


class AbstractProcess:
    """
    abstract process class
    """

    def __init__(self,
                 width=1024,
                 height=768):
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
