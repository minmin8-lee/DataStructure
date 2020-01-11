from Stack import Container


class Stack(Container.Container):
    def __init__(self,size):
        super().__init__()
        self._size = size

    def push(self, data):
        """
        1. if is_full : end
        2. else : append data
        3. add count and update index
        4. cursor <- __data__[idx]
        :param data: input
        :return: -1 if fails
        """
        if self.is_full():
            print("i'm full.")
            return -1
        else:
            self.__data__.append(data)
            self._add_count()
            self._cursor = self.__data__[self._index]

    def pop(self):
        """
        1. if is empty -> end
        else
        2. to_pop = _cursor
        3. del data[idx]
        4. subtract count and update index
        5. cursor <- data[idx]
        :return: to_pop
        """
        if self.is_empty():
            print("i'm hungry")
            return -1
        else:
            to_pop = self._cursor
            del self.__data__[self._index]
            self._sub_count()
            self._cursor = self.__data__[self._index]
            return to_pop
