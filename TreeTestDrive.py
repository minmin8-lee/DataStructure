from Tree.BinarySearchTree import BST
from Tool.func import random_list_generator

bst = BST()
lst = random_list_generator(0, 10, 30)
for n in lst:
    bst.insert(n)

bst.search(1)
bst.search(11)

bst.in_order_traversal()  # BST에서 중위순회시 오름차순이 됨
bst.pre_order_traversal()
bst.post_order_traversal()


from Tree.AVLTree import AVLT

avl = AVLT()
lst = random_list_generator(0, 10, 30)
for n in lst:
    avl.insert(n)

avl.in_order_traversal()  # BST에서 중위순회시 오름차순이 됨
avl.pre_order_traversal()
avl.post_order_traversal()


from Tree.RedBlackTree import RBT

rb1 = RBT()
lst = random_list_generator(0, 10, 30)
for n in lst:
    rb1.insert(n)

rb1.in_order_traversal()  # BST에서 중위순회시 오름차순이 됨
rb1.pre_order_traversal()
rb1.post_order_traversal()
