# 实现单链表的基本操作并测试（自选带头结点的或者不带头结点的链表形式），链表方法包括：
# __init__(self)
# is_empty(self)
# add(self，data)   #头插法
# insert(self,  pos,  data)  #任意位置下标pos插入数据
# remove(self,  data)  #删除首次出现的数据data
# display(self)
# size(self)  #求链表实际长度，不含头结点

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert(self, pos, data):
        if pos <= 0:
            self.add(data)
        else:
            node = Node(data)
            pre = self.head
            count = 0
            while count < pos - 1 and pre:
                pre = pre.next
                count += 1
            if not pre:
                raise IndexError("Index out of range")
            node.next = pre.next
            pre.next = node

    def remove(self, data):
        pre = None
        cur = self.head
        while cur and cur.data != data:
            pre = cur
            cur = cur.next
        if not cur:
            raise ValueError("Data not in list")
        if not pre:
            self.head = cur.next
        else:
            pre.next = cur.next

    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next
        print()

    def size(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count
