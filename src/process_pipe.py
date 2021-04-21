# coding=utf-8
# author xin.he

class ImgTailorPipeLine:

    def __init__(self, process_list):
        assert process_list is not None
        assert isinstance(process_list, list)

        self._process_list = process_list

    def exec(self):

        for f in self._process_list:
            f()


def process_001():
    print(1)


def process_002():
    print(2)


if __name__ == '__main__':

    process_list = [process_001, process_002]

    itP = ImgTailorPipeLine(process_list)
    itP.exec()
