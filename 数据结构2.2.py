
class queue:
    def __init__(self,maxmize):
        self.maxmize = maxmize
        self.items=[0]*maxmize
        self.front=0
        self.rear=0
    def is_empty(self):
        return self.front ==self.rear
    def is_full(self):
        return (self.rear+1)%len(self.items)==self.front
    def size(self):
        return (self.rear-self.front+len(self.items))%self.maxmize
    def enqueue(self,item):
        if not self.is_full():
            self.items[self.rear]=item
            self.rear=(self.rear+1)%self.maxmize
        else:
            raise IndexError("Quene is full")
    def dequeue(self):
        if not self.is_empty():
            it=self.items[self.front]
            self.front=(self.front+1)%self.maxmize
            return it
        else:
            raise IndexError("Quene is empty")
    def display(self):
        i=self.front
        while i!=self.rear:
            print(self.items[i],end='')
            i=(i+1)%self.maxmize
        print()
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
    def display(self):
        print(self.items)
n,i=map(int,input().split())
parking=Stack()
waiting=queue(n)
for j in range(1,n+1):
    parking.push(j)
for k in range(1,n-i+1):
    waiting.enqueue(parking.pop())
parking.pop()
for l in range(1,waiting.size()+1):
    parking.push(waiting.dequeue())
parking.display()

