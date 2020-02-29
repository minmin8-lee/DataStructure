from Tree.BinarySearchTree import BST


class AVLT(BST):
    def __init__(self):
        super().__init__()

    def insert(self, data, node=None):
        last_node = self.__insert__(data, node)
        self.__update_bf__(last_node)

    def __update_bf__(self, node):
        """
        기본값을 0점으로 두고,
        root에 도달할 때 까지 balance factor 업데이트
        삽입된 노드가 좌측노드일 경우 +1점, 우측노드일 경우 -1점
        """
        if abs(node.get_bf()) >= 2:
            self.__rebalance__(node)
            return node

        if node.get_parent() is not None:
            if node.get_parent().get_left() == node:
                node.get_parent().add_bf()
                self.__update_bf__(node.get_parent())

            elif node.get_parent().get_right() == node:
                node.get_parent().sub_bf()
                self.__update_bf__(node.get_parent())
            else:
                raise TypeError
        else:
            return

    def __rebalance__(self, node):
        """
            AVL Tree의 Rebalancing 작업 : Rotation 수행
            only 4 cases
            __rotate_left__
            __rotate_right__
            __rotate_left_right__ : 기준 node의 bf > 1 && 왼쪽 자식노드의 bf < 0
            __rotate_right_left__ : 기준 node의 bf < 1 && 오른쪽 자식노드의 bf > 0
        """
        if node.get_bf() > 1:
            if node.get_left().get_bf() < 0:
                self.__rotate_left__(node.get_left())
            self.__rotate_right__(node)

        elif node.get_bf() < -1:
            if node.get_right().get_bf() > 0:
                self.__rotate_right__(node.get_right())
            self.__rotate_left__(node)
        else:
            print("not happened")
            pass

    def __rotate_left__(self, node):
        """
        진입 ) 기준 node의 bf =< -2

        조건1) let 인자로 받은 node를 A(받는 당시 기준 root)
        조건2) let A의 우측 자식노드를 B
        조건3) let B의 좌측 자식노드를 Z

        수행순서
        1) B를 새로운 root 로 선정
        2) A를 B의 좌측 자식으로
        3) Z는 A의 우측 자식으로
        4) 나머지 hierarchy 는 건드리지 않음
        """

        a = node
        b = node.get_right()
        z = b.get_left()

        # procedure 1
        #
        if a.get_parent() is not None:
            if a.get_parent().get_right() == a:
                a.get_parent().change_right(b)
            elif a.get_parent().get_left() == a:
                a.get_parent().change_left(b)
            else:
                raise TypeError
            b.set_parent(a.get_parent())
        else:
            self.__root__ = b
            b.set_parent(None)

        # procedure 2
        b.change_left(a)
        a.set_parent(b)
        a.set_bf(a.get_bf() + 1 - min(0, b.get_bf()))  # 수식 유도를 통해 증명가능.
        b.set_bf(b.get_bf() + 1 + max(a.get_bf(), 0))

        # procedure 3
        a.change_right(z)
        if z is not None:
            z.set_parent(a)
        self.__reset_bf__()

    def __rotate_right__(self, node):
        """
        진입 ) 기준 node의 bf >= 2 만족시

        조건1) let 인자로 받은 node를 A(받는 당시 기준 root)
        조건2) let A의 좌측 자식노드를 B
        조건3) let B의 우측 자식노드를 Z

        수행순서
        1) B를 새로운 root 로 선정
        2) A를 B의 우측 자식으로
        3) Z는 A의 좌측 자식으로
        4) 나머지 hierarchy 는 건드리지 않음
        """
        a = node
        b = node.get_left()
        z = b.get_right()

        # procedure 1
        if a.get_parent() is not None:
            if a.get_parent().get_right() == a:
                a.get_parent().change_right(b)
            elif a.get_parent().get_left() == a:
                a.get_parent().change_left(b)
            else:
                raise TypeError
            b.set_parent(a.get_parent())
        else:
            self.__root__ = b
            b.set_parent(None)

        # procedure 2
        b.change_right(a)
        a.set_parent(b)
        a.set_bf(a.get_bf() - 1 - max(0, b.get_bf()))  # 수식 유도를 통해 증명가능.
        b.set_bf(b.get_bf() - 1 - max(0, a.get_bf()))

        # procedure 3
        a.change_left(z)
        if z is not None:
            z.set_parent(a)
        self.__reset_bf__()

    def __reset_bf__(self):
        self.in_order_traversal()
        for node in self.__traverse_list__:
            if node.is_empty():
                node.set_bf(0)

