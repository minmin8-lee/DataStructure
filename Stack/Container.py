class Container:
    def __init__(self):
        self.__data__ = []
        self._size = None
        self._count = 0
        self._index = self._count - 1
        self._cursor = None

    def _reset_index(self):
        self._index = self._count - 1

    def _add_count(self):
        self._count += 1
        self._reset_index()

    def _sub_count(self):
        self._count -= 1
        self._reset_index()

    def peek(self):
        return self._cursor

    def count(self):
        return self._count

    def is_full(self):
        if self._count == self._size:
            return True
        else:
            return False

    def is_empty(self):
        if self._count == 0:
            return True
        else:
            return False
