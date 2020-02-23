from Tree.Node import Node


class BST:
    def __init__(self):
        self.__root__ = None
        self.__cursor__ = None

    def __reset__(self):
        # 커서를 루트로 초기화
        self.__cursor__ = self.__root__

    def __locate_cursor__(self, node):
        # 받은노드로 커서이동
        self.__cursor__ = node

    def insert(self, data, node=None):
        # 텅 비었으면 삽입후 종료(root)
        if self.__root__ is None:
            self.__root__ = Node(data)
            self.__root__.set_level(0)
            self.__reset__()
            return 0

        else:
            if node is None:
                node = self.__root__
            self.__locate_cursor__(node)
            cnt = self.__cursor__.get_level()

            # 해당 노드값 > 데이터 : 왼쪽노드 확인
            if self.__cursor__.get_data() > data:
                if self.__cursor__.get_left() is None:  # 왼쪽노드 비었으면 삽입
                    self.__cursor__.set_left(data, cnt+1)
                    self.__reset__()
                    return 0
                else:  # 아니면 왼쪽노드의 다음노드 확인후 반복
                    self.insert(data, self.__cursor__.get_left())

            # 해당 노드값 < 데이터 : 오른쪽노드 확인
            elif self.__cursor__.get_data() < data:
                if self.__cursor__.get_right() is None:  # 오른쪽노드 비었으면 삽입
                    self.__cursor__.set_right(data, cnt+1)
                    self.__reset__()
                    return 0
                else:  # 아니면 오른쪽노드의 다음노드 확인후 반복
                    self.insert(data, self.__cursor__.get_right())

            # BST에서는 중복된 값을 주면 천벌을 내린다
            else:
                print("duplicated input! take this! judgment of THE GOD of fire!")
                return -1

    def search(self, data):
        # 커서에 원하는값이 있는지 확인 (모든 연산 뒤 커서는 무조건 root로 초기화되어있음)
        if self.__cursor__.get_data() == data:
            print("found at level", self.__cursor__.get_level())
            temp = self.__cursor__
            self.__reset__()
            return temp

        else:
            # 커서의 값 > 데이터인 경우 커서를 왼쪽으로 보내서 찾기
            # 다음 왼쪽이 없으면 다왔는데 못찾은거
            if self.__cursor__.get_data() > data:
                if self.__cursor__.get_left() is None:
                    print("not found")
                    self.__reset__()
                    return -1
                self.__locate_cursor__(self.__cursor__.get_left())
                return self.search(data)
            # 커서의 값 < 데이터인 경우 커서를 오른쪽으로 보내서 찾기 (같은경우는 애시당초 X)
            # 다음 오른쪽이 없으면 다왔는데 못찾은거
            else:
                if self.__cursor__.get_right() is None:
                    print("not found")
                    self.__reset__()
                    return -1
                self.__locate_cursor__(self.__cursor__.get_right())
                return self.search(data)

    def in_order_traversal(self):
        self.__in_order_traversal__(self.__root__)

    def __in_order_traversal__(self, node):
        if node is not None:
            self.__in_order_traversal__(node.get_left())
            print(node.get_data())
            self.__in_order_traversal__(node.get_right())

    def pre_order_traversal(self):
        return self.__pre_order_traversal__(self.__root__)

    def __pre_order_traversal__(self, node):
        if node is not None:
            print(node.get_data())
            self.__pre_order_traversal__(node.get_left())
            self.__pre_order_traversal__(node.get_right())

    def post_order_traversal(self):
        self.__post_order_traversal__(self.__root__)

    def __post_order_traversal__(self, node):
        if node is not None:
            self.__post_order_traversal__(node.get_left())
            self.__post_order_traversal__(node.get_right())
            print(node.get_data())
