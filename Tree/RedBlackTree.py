from Tree.BinarySearchTree import BST
from Tree.Node import Node


class RBT(BST):
    def __init__(self):
        super().__init__()

    def insert(self, data, node=None):
        last_node = self.__insert__(data, node)

        if last_node.get_parent() is None:
            last_node.set_color(False)
        else:
            last_node.set_color(True)
            # 더블레드일 경우, 삼촌노드 확인 필수
            self.__check_double_red__(last_node)

        print(last_node.get_color())
        self.pre_order_traversal()

    def __check_double_red__(self, node):
        if node.get_parent() is None:
            raise LookupError("여기서 호출되시면 안됩니다. 더블레드찾기 잘못된 호출.")

        # 더블레드 확인
        if node.get_color() and node.get_parent().get_color():
            # 삼촌이 레드
            if self.__check_uncle__(node):
                self.__recolor__(node)
            # 삼촌이 블랙
            else:
                self.__reconstruct__(node)

        # 더블레드가 아님
        else:
            pass

    @staticmethod
    def __check_uncle__(node):
        if node.get_grand_parent() is None:
            raise LookupError("여기서 호출되시면 안됩니다. 삼촌찾기 잘못된 호출.")
        else:
            if node.get_uncle() is None:
                return False
            else:
                return node.get_uncle().get_color()

    def __reconstruct__(self, node):
        gp = node.get_grand_parent()
        p = node.get_parent()
        lst = [node, p, gp]
        sorted_lst = []

        # 간단한 sort로 정렬
        while len(lst) > 1:
            if lst[0].get_data() > lst[1].get_data():
                sorted_lst.append(lst.pop(1))
            else:
                sorted_lst.append(lst.pop(0))

        sorted_lst.append(lst.pop(0))
        if sorted_lst[0].get_data() > sorted_lst[1].get_data():
            tmp = sorted_lst[1]
            sorted_lst[1] = sorted_lst[0]
            sorted_lst[0] = tmp

        for d in sorted_lst:
            print("ㅇㅇ : ", d.get_data())

        # sorted_lst = [민, 중간, 맥스]
        # 중간이 부모가되고 나머지는 새끼가 됨
        if gp == self.__root__:
            print("grandpa : ", gp.get_data())
            self.__reconnect_node__(parent=sorted_lst[1], left_child=sorted_lst[0])
            self.__reconnect_node__(parent=sorted_lst[1], right_child=sorted_lst[2])

            self.pre_order_traversal()
            for d in self.__traverse_list__:
                print((d.get_data(), d.get_color()))

            sorted_lst[1].set_parent(None)
            self.__root__ = sorted_lst[1]
        else:
            if gp.is_left_child():
                gp.get_parent().change_left(sorted_lst[1])
                sorted_lst[1].set_parent(gp.get_parent())
            else:
                gp.get_parent().change_right(sorted_lst[1])
                sorted_lst[1].set_parent(gp.get_parent())

            self.__reconnect_node__(parent=sorted_lst[1], left_child=sorted_lst[0])
            self.__reconnect_node__(parent=sorted_lst[1], right_child=sorted_lst[2])

        # 노드순서를 바꿨는데 새끼노드간의 관계가 남아있는 경우 제거
        # 큰애의 왼쪽이 작은애인 케이스
        # 작은애의 오른쪽이 큰애인 케이스 뿐
        # 나머지 연결관계는 손대면 안됨 (예) 큰애의 오른쪽 서브트리, 작은애의 왼쪽 서브트리
        if sorted_lst[2].get_left() == sorted_lst[0]:
            sorted_lst[2].change_left(None)
        elif sorted_lst[0].get_right() == sorted_lst[2]:
            sorted_lst[0].change_right(None)
        else:
            pass

        # 작업종료후 [RED - BLK - RED] 구조로 변경
        sorted_lst[0].set_color(True)
        sorted_lst[1].set_color(False)
        sorted_lst[2].set_color(True)

    def __recolor__(self, node):
        node.get_uncle().set_color(False)
        node.get_parent().set_color(False)
        node.get_grand_parent().set_color(True)

        if node.get_grand_parent().get_parent() is not None:
            self.__check_double_red__(node.get_grand_parent())

        # 부모없는경우 ROOT 까지 갔단 얘기, 이럴때는 다시 Black으로 바꿔줌
        else:
            node.get_grand_parent().set_color(False)

    @staticmethod
    def __reconnect_node__(parent, left_child=None, right_child=None):
        if isinstance(parent, Node) and isinstance(left_child, Node):
            parent_old_left = parent.get_left()
            parent.change_left(left_child)
            left_child.set_parent(parent)
            if left_child.get_right() == parent:
                left_child.change_right(parent_old_left)
                if parent_old_left is not None:
                    parent_old_left.set_parent(left_child)
            if parent.get_grand_parent() == left_child:
                left_child.change_right(parent_old_left)
                if parent_old_left is not None:
                    parent_old_left.set_parent(left_child)
            print("부모와 왼쪽노드 연결 완료")

        elif isinstance(parent, Node) and isinstance(right_child, Node):
            parent_old_right = parent.get_right()
            parent.change_right(right_child)
            right_child.set_parent(parent)
            if right_child.get_left() == parent:
                right_child.change_left(parent_old_right)
                if parent_old_right is not None:
                    parent_old_right.set_parent(right_child)
            if parent.get_grand_parent() == right_child:
                right_child.change_left(parent_old_right)
                if parent_old_right is not None:
                    parent_old_right.set_parent(right_child)
            print("부모와 오른쪽노드 연결 완료")

        else:
            raise TypeError("노드타입을 넣어야지 바꿔주지..")

