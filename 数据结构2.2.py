#有一狭长停车场可停放n辆车，只有一个门可供进出。车辆按照到达的早晚从最里面依次向外排列，
#若停车场中的车辆1要出来，则在它之后进入停车场的车都要让路，进入暂停区域，等要出场的车辆
#离开后，这些车辆再依次进场。
#例如：停车场由内到外停放了1,2,3,4共4辆车，若车辆2要出场，则车辆4，车辆3需要依次进入
#暂停区域，车辆2离开后，车辆4和车辆3通过暂停区域（环形车道）再次进入停车场，此时停车场
#由内到外停放情况为：车辆1，车辆4，车辆3。
#基于上述背景，编写车辆调度程序，实现以下功能：
#1.由用户指定停车场内总的车辆数n及第 i 辆车出停车场；
#2.输出以下两个时刻车辆的调度情况：
# 1）依次输出需要驶入暂停区域的车辆
# 2）第 i 辆车开出后，暂停区域的车辆重新回到停车场，此时停车场中的车辆。
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
        self.items.pop()

    # 观察
    def peek(self):
        return self.items[-1]

    # 栈元素数量
    def size(self):
        return len(self.items)
    
    #显示
    def display(self):
        print(self.items)

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
            #print("enq",end=" ")
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

s=Stack()
q=Queue()
n=int(input("n:"))
for j in range(1,n+1):
    s.push(j)
i=int(input("i:"))
for j in range(i+1,n+1):
    num=s.peek()
    s.pop()
    print(num,end=" ")
    q.enqueue(num)
s.pop()
for j in range(i+1,n+1):
    num=q.dequeue()
    s.push(num)
print(s.display())