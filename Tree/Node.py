
class Node:
    def __init__(self, data=None):
        self.__data__ = data
        self.__left__ = None
        self.__right__ = None
        self.__level__ = None

    def _set_data_(self, data):
        self.__data__ = data

    def set_left(self, data, cnt):
        self.__left__ = Node(data)
        self.__left__.set_level(cnt)

    def set_right(self, data, cnt):
        self.__right__ = Node(data)
        self.__right__.set_level(cnt)

    def set_level(self, cnt):
        self.__level__ = cnt

    def get_data(self):
        return self.__data__

    def get_left(self):
        return self.__left__

    def get_right(self):
        return self.__right__

    def get_level(self):
        return self.__level__
