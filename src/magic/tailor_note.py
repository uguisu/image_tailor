# coding=utf-8
# author xin.he

class TailorNote:
    """
    Tailor Note class
    """

    def __init__(self):
        self._label = None
        self._points = None

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        assert label is not None and len(str(label)) > 0
        self._label = label

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, points):
        assert points is not None and isinstance(points, list)
        self._points = points

    def __str__(self):
        return '[label]=%s; [points]=%s' % (self._label, self._points)
