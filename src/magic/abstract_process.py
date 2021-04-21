# coding=utf-8
# author xin.he

class AbstractProcess:
    """
    abstract process class
    """

    def __init__(self):
        pass

    def process(self, loop=0):
        """
        process
        :param loop: how many times to loop
        :return: image object as list
        """
        raise RuntimeError('use implement class')
