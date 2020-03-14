
class Node:
    def __init__(self, data=None):
        self.__data__ = data
        self.__left__ = None
        self.__right__ = None
        self.__parent__ = None
        self.__level__ = None

        # for AVLT
        self.__bf__ = 0

        # for RBT
        self.__color__ = None

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

    def is_left_child(self):
        if self.get_parent() is None:
            raise KeyError("엄마없음")
        if self.get_parent().get_left() == self:
            return True
        elif self.get_parent().get_right() == self:
            return False
        else:
            raise ValueError("왼쪽자식도 오른쪽자식도 아니면 누구자식? 메모리오류")

    """
    Belows required for RBT Implementation
    """

    def get_grand_parent(self):
        if self.get_parent() is None:
            return None
        else:
            # parent 없는 경우가 처리되었으므로, parent의 parent가 없는 경우는 알아서 return None. 호출문재X
            return self.get_parent().get_parent()

    def get_uncle(self):
        if self.get_parent() is None:
            return None
        elif self.get_grand_parent() is None:
            return None
        else:
            # 내 부모가 왼쪽 자식이면 할배의 오른쪽이 삼촌
            if self.get_parent().is_left_child():
                return self.get_grand_parent().get_right()
            # 내 부모가 오른쪽 자식이면 할배의 왼쪽이 삼촌
            else:
                return self.get_grand_parent().get_left()

    def get_color(self):
        if self.__color__ is None:
            return False
        else:
            return self.__color__

    def set_color(self, color):
        if isinstance(color, bool):
            self.__color__ = color
        else:
            raise TypeError("got wrong color. check color type. True: Red, False: Black")
