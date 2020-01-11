class Array:
    """
    cf. dynamic size !
    """
    def __init__(self, data=None):
        self.__data__ = []
        self._size = None
        self._setup(data)

    def _setup(self, data):
        if data is None:
            self.__data__ = []
            self._size = 0
        else:
            # 입력이 리스트나 튜플
            if isinstance(data,type([])) or isinstance(data,type(())):
                self._size = len(data)
                self._update_data(data)
            # 입력이 딕셔너리 -> 안받아 돌아가
            elif data is dict([]):
                print("dict not allowed")
                raise KeyError
            # 입력이 단일값
            else:
                self._size = 1
                self._update_data([data])

    def _update_size(self):
        self._size = len(self._get_data())

    def _get_data(self):
        return self.__data__

    def _update_data(self, data):
        self.__data__ = data

    @staticmethod
    def _index_type_checker(idx):
        if isinstance(idx,type(1)):
            return idx
        else:
            print(idx, " is not allowed. may not be work properly.")

    def is_empty(self):
        if self._size < 1:
            return True
        else:
            return False

    def traverse(self):
        """
        1. if is_empty(): end
        else:
        2. while i =< size
            print __data__[i]
        3. end
        :return: None
        """
        if self.is_empty():
            print("EMPTY")
            return -1
        else:
            i = 0
            while i < self._size:
                print(self.__data__[i])
                i += 1

    def insertion(self, new_data, idx=0):
        if self._size == 0:
            a = self._get_data()
            a.append(new_data)
            self._update_data(a)
            self._update_size()
            print("start from scratch!")
            return 1
        idx = self._index_type_checker(idx)
        a = self._get_data()
        # case 1. Head
        if idx == 0:
            a = [new_data]
            for i in range(self._size):
                a.append(self.__data__[i])
            self._update_data(a)
            self._update_size()
            print("head insertion")
            return 2
        # case 2. 0 < idx < size
        # 뒤에서부터 작업하면, size ~ idx 까지만 계산 가능하여 평균 TC 감소 가능
        elif (0 < idx) and (idx < self._size):
            a.append("dummy")
            i = self._size-1
            while i >= idx:
                a[i+1] = a[i]
                i -= 1
            a[i+1] = new_data
            self._update_data(a)
            self._update_size()
            print("inserted at idx no. ", idx)
            return 3
        # case 3. tail
        elif idx == self._size:
            a = self._get_data()
            a.append(new_data)
            self._update_data(a)
            self._update_size()
            print("inserted at tail.")
            return 4
        else:
            raise IndexError("Invalid index. input index : %d, size of array: %d." %(idx, self._size))

    def deletion(self,idx=0):
        """
        1. if is_empty: raise ValueError("EMPTY")
        2. if idx == 0 (head) : goto 3
           elif 0 < idx < size : goto 5
           elif idx == size-1(tail): goto 8
           else: raise IndexError("idx out of range")

        3. for i in range(1,size):
            dummy.append(__data__[i])
        4. _update_data(dummy),_update_size(), goto end

        5. for i in range(idx):
            dummy.append(__data__[i])
        6. for i in range(idx+1, size):
            dummy.append(__data__[i])
        7. _update_data(dummy), _update_size(), goto end

        8. dummy = _get_data()
        9. dummy.pop()
        10. _update_data(dummy), _update_size()
        11. end
        :param idx: INDEX
        :return: None
        """
        if self.is_empty() : raise ValueError("EMPTY!!!!!")
        idx = self._index_type_checker(idx)
        if idx == 0:
            a = [self.__data__[i] for i in range(1,self._size)]
            self._update_data(a)
            self._update_size()
            print("deleted head")
            return 0
        elif (0 < idx) and (idx < self._size):
            a = [self.__data__[i] for i in range(0,idx)]
            for i in range(idx+1, self._size):
                a.append(self.__data__[i])
            self._update_data(a)
            self._update_size()
            print("deleted data at idx no. %d"%idx)
            return 1
        elif idx == self._size-1:
            a = self._get_data()
            a.pop()
            self._update_data(a)
            self._update_size()
            print("deleeeeeted tail")
            return 2
        else:
            raise IndexError("Invalid index. input index : %d, size of array: %d." %(idx, self._size))

    def search(self,target_data):
        if self.is_empty(): raise ValueError("EMPTY!!!!!!!! ")
        for i in range(self._size):
            if target_data == self.__data__[i]:
                return i
            else:
                continue
        print("NOT FOUND")
        return -1

    def update(self, data, idx):
        if self.is_empty(): raise ValueError("EMPTY!!!!!!!! ")
        elif (0 > idx) or (idx >= self._size):
            raise IndexError("Invalid index. input index : %d, size of array: %d." %(idx, self._size))
        else:
            idx = self._index_type_checker(idx)
            a = self._get_data()
            a[idx] = data
            self._update_data(a)
            print(idx, "th data changed into", data)
