# coding=utf-8
# author xin.he
import os


class ImagesLoader:
    """
    Load images from folder, skip empty folder
    """

    def __init__(self, folder):
        assert folder is not None
        assert isinstance(folder, str)

        self._folder = folder

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
                rtn.append(sub_path)

        return rtn

    def load_file_list(self):
        """
        load file list
        :return: file list
        """
        return self._load_file_list(self._folder)
