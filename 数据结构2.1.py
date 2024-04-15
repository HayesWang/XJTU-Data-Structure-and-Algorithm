#实现循环队列基本操作并测试，需实现以下方法：
#__init__(),  is_empty(),   is_full()
#enqueue() ,  dequeue(),   display() ,  size()  
class Queue:
    def __init__(self,maxSize=101):
        self.maxSize=maxSize
        self.items=[0]*maxSize
        self.front=0
        self.rear=0
    def enqueue(self,item):
        if not self.is_full():
            self.rear=(self.rear+1)%self.maxSize
            self.items[self.rear]=item
            print("enq",end=" ")
        else:
            print("Full")
    def dequeue(self):
        if not self.is_empty():
            self.front=(self.front+1)%self.maxSize
            return self.items[self.front]
    def is_full(self):
        return (self.rear + 1)%self.maxSize == self.front
    def is_empty(self):
        return self.items==[]
    def display(self):
        ctr=self.front
        while True: 
            ctr = (ctr+1)%self.maxSize
            print(self.items[ctr])
            if ctr==self.rear:
                break
    def size(self):
        return (self.rear-self.front+self.maxSize)%self.maxSize
            

q = Queue()
#0,50 正常输入输出
for i in range(0,50):
    q.enqueue(i)
print("")
for i in range(0,50):
    print(q.dequeue(),end=" ")
print("")
#再输入100个，测试循环性
for i in range(0,100):
    q.enqueue(i)
print("")
for i in range(0,100):
    print(q.dequeue(),end=" ")
#输入125个，测试溢出
for i in range(0,120):
    q.enqueue(i)
#测试display,size
q.display()
print("size: ",q.size())