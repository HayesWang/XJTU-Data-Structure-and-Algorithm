from Lib.Stack import Stack

class Node:
    def __init__(self, data=None):
        self.data = data
        self.lchild = None
        self.rchild = None


class BinaryTree:
    def __init__(self):
        self.root = None
    def insertLeft(self,parent,data):
        node = Node(data)
        node.lchild = parent.lchild
        parent.lchild = node
    def insertRight(self,parent,data):
        node = Node(data)
        node.rchild = parent.rchild
        parent.rchild = node
    def get_root_val(self):
        if self.root:
            return self.root.data
        else:
            return None
    def set_root_val(self,data):
        if self.root:
            self.root.data = data
        else:
            self.root = Node(data)
    def get_left_child(self, parent):
        return parent.lchild if parent else None
    def get_right_child(self, parent):
        return parent.rchild if parent else None

    def preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.preorder(node.lchild)
            self.preorder(node.rchild)

    def inorder(self, node):
        if node:
            self.inorder(node.lchild)
            print(node.data, end=' ')
            self.inorder(node.rchild)

    def postorder(self, node):
        if node:
            self.postorder(node.lchild)
            self.postorder(node.rchild)
            print(node.data, end=' ')

    def no_rec_preorder(self,root):
        if root == None:
            return
        stack = Stack()
        node = root
        while not stack.is_empty():
            print(node.data,end=',')
            if node.rchild:
                stack.push(node.rchild)
            if node.lchild:
                node = node.lchild
            else:
                node = stack.pop()




