# coding=utf-8
# author xin.he
from share import Exclusion


class JsonFilter(Exclusion):
    """
    Json file filter
    """
    def __init__(self, next_filter=None):
        super().__init__(next_filter=next_filter)

    def exec(self, file_name_as_string):
        """
        override exec()
        :param file_name_as_string:
        :return: True - find problem
        """
        return file_name_as_string.endswith('.json')
