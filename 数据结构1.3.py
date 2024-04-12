class Stack:
    def __init__(self):
        self.items = []
    #入栈操作
    def push(self, item):
        self.items.append(item)
    #出栈操作
    def pop(self):
        return self.items.pop()
    #查看栈顶元素
    def peek(self):
        return self.items[-1]
    #判断栈是否为空
    def is_empty(self):
        return self.items == []
    #获取栈的大小
    def size(self):
        return len(self.items)
    #显示
    def display(self):
        print(self.items)
def Xiaoxiaole(exstring):
    stack = Stack()
    stack.push(exstring[0])
    for i in range(1, len(exstring)):
        if(exstring[i] == exstring[i-1]):
            stack.pop()
        else:stack.push(exstring[i])
    stack.display()
a = Xiaoxiaole(input())
print(a)