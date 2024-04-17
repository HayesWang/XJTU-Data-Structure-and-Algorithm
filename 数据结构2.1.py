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
        return self.front==self.rear
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

#class quene:
#     def __init__(self,maxmize):
#         self.maxmize = maxmize
#         self.items=[0]*maxmize
#         self.front=0
#         self.rear=0
#     def is_empty(self):
#         return self.front ==self.rear
#     def is_full(self):
#         return (self.rear+1)%len(self.items)==self.front
#     def size(self):
#         return (self.rear-self.front+len(self.items))%self.maxmize
#     def enqueue(self,item):
#         if not self.is_full():
#             self.items[self.rear]=item
#             self.rear=(self.rear+1)%self.maxmize
#         else:
#             raise IndexError("Quene is full")
#     def dequeue(self):
#         if not self.is_empty():
#             it=self.items[self.front]
#             self.front=(self.front+1)%self.maxmize
#             return it
#         else:
#             raise IndexError("Quene is empty")
#     def display(self):
#         i=self.front
#         while i!=self.rear:
#             print(self.items[i],end='')
#             i=(i+1)%self.maxmize
#         print()
# 
# #测试
# q=quene(4)
# print(q.is_empty())
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q.is_full())
# q.display()
# print(q.dequeue())
# q.display()
# print(q.size())
