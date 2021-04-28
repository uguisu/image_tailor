# coding=utf-8
# author xin.he
import os


class ImagesLoader:
    """
    Load images from folder, skip empty folder
    """

    def __init__(self,
                 folder,
                 stander_width=None,
                 stander_height=None,
                 filter_chain=None):
        assert folder is not None and isinstance(folder, str)
        assert (filter_chain is None) or (filter_chain is not None and isinstance(filter_chain, Exclusion))

        self._folder = folder
        self._stander_width = stander_width
        self._stander_height = stander_height
        self._filter_chain = filter_chain

        # load file list
        self._file_list = self._load_file_list(self._folder)

    def _load_file_list(self, root_path=None):
        """
        load file list
        :param root_path: root path
        :return: file list
        """
        if root_path is None:
            return

        rtn = []

        # get sub folder list
        files_and_folders = os.listdir(root_path)

        for file_name in files_and_folders:

            # try to get sub path
            sub_path = os.path.join(root_path, file_name)

            # fetch images
            if os.path.isdir(sub_path):
                rtn.extend(self._load_file_list(sub_path))
            else:
                # exclude some file
                if self._filter_chain is not None and self._filter_chain.filter(sub_path):
                    continue
                rtn.append(sub_path)

        return rtn

    @DeprecationWarning
    def load_file_list(self):
        """
        load file list
        :return: file list
        """
        return self._file_list

    @property
    def file_list(self):
        return self._file_list

    @property
    def stander_width(self):
        return self._stander_width

    @property
    def stander_height(self):
        return self._stander_height


class Exclusion:
    """
    Exclusion

    Exclusion is a linked list
    """
    def __init__(self, next_filter=None):
        # verify
        assert next_filter is None or isinstance(next_filter, Exclusion)

        self._next_filter = next_filter

    def filter(self, file_name_as_string):
        """
        filter
        :param file_name_as_string: file name as string
        :return: True - find problem
        """
        if file_name_as_string is None or '' == file_name_as_string:
            return False

        # execute
        if self.exec(file_name_as_string):
            return True
        else:
            # call next filter
            if self._next_filter is not None:
                return self._next_filter.filter(file_name_as_string)

    def exec(self, file_name_as_string):
        """
        execute
        :param file_name_as_string: file name as string
        :return: True - find problem
        """
        raise RuntimeError('use implement class')
