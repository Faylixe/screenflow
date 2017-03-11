#!/usr/bin/python


class Sizer(object):
    """
    """

    def __init__(self, object, sizer):
        """Default constructor.

        :param data:
        """
        self.data = data
        self.sizer = sizer
        self._size = None

    @property
    def size(self):
        """
        :returns:
        """
        if self._size is None:
            self._size = self.sizer(data)
        return self._size