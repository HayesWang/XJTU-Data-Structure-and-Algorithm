# 可以将普通二叉树补足成完全二叉树，将节点从0开始从上到下、从左至右依次进行编号，补足的附加结点用#表示。
# 输入补足的完全二叉树的字符串形式，如 " AB##C"，构造相应的链式二叉树，并实现先序、中序和后序的遍历函数。对相关代码进行测试
# 示例：
# 【输入】“AB##C”
# 【输出】
# 先序 A B C
# 中序 B C A
# 后序 C B A

from Lib.BiTree import Node
from Lib.BiTree import BinaryTree

def appendNode(node, data, number, level):


tree = BinaryTree()
global ctr
ctr = 0
data = input("Please input the data of the complete binary tree:")

print("Preorder:")
tree.preorder(tree.root)
print()
print("Inorder:")
tree.inorder(tree.root)
print()
print("Postorder:")
tree.postorder(tree.root)
print()
