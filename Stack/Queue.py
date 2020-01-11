from Stack.Container import Container


class Queue(Container):
    def __init__(self, size):
        super().__init__()
        self._size = size

    def __insert_head__(self,data):
        current_data = self.__data__
        new_data = [data]

        for unit_old_data in current_data:
            new_data.append(unit_old_data)
        self.__data__ = new_data

    def enqueue(self,data):
        """
        1. if is_full : end
        else :
        2. append data at the head of __data__
        3. add_count and update cursor idx
        4. cursor <- __data__[idx]

        :param data: data to insert
        :return: -1 iferror
        """
        if self.is_full():
            print("i'm full")
            return -1
        else:
            self.__insert_head__(data)
            self._add_count()
            self._cursor = self.__data__[self._index]

    def dequeue(self):
        """
        1. if is_empty : end
        else:
        2. to_pop = _cursor
        3  del __data__[idx]
        4. sub_count and update cursor idx
        5. cursor <- __data__[idx]
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
