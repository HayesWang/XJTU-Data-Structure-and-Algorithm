class Stack:
    def __init__(self):
        self.items = []

    # 入栈
    def push(self, item):
        self.items.append(item)

    # 判断为空？
    def is_empty(self):
        return self.items == []

    # 出栈
    def pop(self):
        return self.items.pop()

    # 观察
    def peek(self):
        return self.items[-1]

    # 栈元素数量
    def size(self):
        return len(self.items)