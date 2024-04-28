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

