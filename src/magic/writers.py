# coding=utf-8
# author xin.he
from magic import TailorNote


class IcdarWriter:

    def __init__(self,
                 image_path=''):
        """
        :param image_path: image path
        """

        # verify
        assert image_path is None or (image_path is not None and isinstance(image_path, str))

        self._image_path = image_path

        # init
        self._image_info_array = []

    @property
    def image_path(self):
        return self._image_path

    @image_path.setter
    def image_path(self, image_path):
        assert image_path is not None and isinstance(image_path, str)
        self._image_path = image_path

    def add(self, image_info):
        """
        cache image info
        :param image_info: TailorNote object
        """
        # verify
        assert isinstance(image_info, TailorNote)
        self._image_info_array.append(image_info)

    def exec(self, image_as_array=None):

        # verify
        if self._image_info_array is None or 0 == len(self._image_info_array):
            return None
        if image_as_array is None:
            return None

        wrk_label = []
        for img in self._image_info_array:
            wrk_label.append({
                'transcription': img.label,
                'points': img.points
            })

        return {
            'img': image_as_array,
            'label': wrk_label
        }
