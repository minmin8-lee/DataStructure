
class Node:
    def __init__(self, data=None):
        self.__data__ = data
        self.__left__ = None
        self.__right__ = None
        self.__parent__ = None
        self.__level__ = None
        self.__bf__ = 0

    def _set_data_(self, data):
        self.__data__ = data

    def set_left(self, data, cnt):
        self.__left__ = Node(data)
        self.__left__.set_level(cnt)

    def set_right(self, data, cnt):
        self.__right__ = Node(data)
        self.__right__.set_level(cnt)

    def change_left(self, node):
        if isinstance(node, Node):
            self.__left__ = node
        elif node is None:
            self.__left__ = None
        else:
            raise TypeError

    def change_right(self, node):
        if isinstance(node, Node):
            self.__right__ = node
        elif node is None:
            self.__right__ = None
        else:
            raise TypeError

    def set_parent(self, node):
        # AVL Tree의 경우 부모노드의 정보를 갖고있어야 BF 계산시 time complexity 감소 가능
        # 데이터 1개분의 공간복잡도 상승은 덤
        if isinstance(node, Node):
            self.__parent__ = node
        elif node is None:
            self.__parent__ = None
        else:
            raise TypeError

    def set_bf(self, val):
        # dangerous ! be careful !!
        self.__bf__ = val

    def add_bf(self):
        self.__bf__ += 1

    def sub_bf(self):
        self.__bf__ -= 1

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

    def get_parent(self):
        return self.__parent__

    def get_bf(self):
        return self.__bf__

    def is_empty(self):
        if self.get_left() is None and self.get_right() is None:
            return True

        else:
            return False
