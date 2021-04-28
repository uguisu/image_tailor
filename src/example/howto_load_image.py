# coding=utf-8
# author xin.he
from share import ImagesLoader, Exclusion


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


class CorgiFilter(Exclusion):
    """
    Corgi file filter
    """
    def __init__(self, next_filter=None):
        super().__init__(next_filter=next_filter)

    def exec(self, file_name_as_string):
        """
        override exec()
        :param file_name_as_string:
        :return: True - find problem
        """
        return file_name_as_string.find("corgi") >= 0


def example_001():
    # all files under 'images' will be load
    il = ImagesLoader('./images/')
    rtn_list = il.file_list
    for f in rtn_list:
        print('f1 = ', f)


def example_002():
    # to load images under sub-folder
    il = ImagesLoader('./images/corgi/')
    rtn_list = il.file_list
    for f in rtn_list:
        print('f2 = ', f)


def example_003():
    """
    load image with filter chain
    """
    # declare a "json file" filter
    jf = JsonFilter()

    il = ImagesLoader('./images/', filter_chain=jf)
    rtn_list = il.file_list
    for f in rtn_list:
        print('f3 = ', f)


def example_004():
    """
    load image with filter chain
    """
    # declare a "corgi" filter
    corgi_filter = CorgiFilter()
    # declare a "json" filter
    jf = JsonFilter(next_filter=corgi_filter)

    il = ImagesLoader('./images/', filter_chain=jf)
    rtn_list = il.file_list
    for f in rtn_list:
        print('f4 = ', f)


if __name__ == '__main__':
    example_001()
    print("-" * 10)
    example_002()
    print("-" * 10)
    example_003()
    print("-" * 10)
    example_004()
