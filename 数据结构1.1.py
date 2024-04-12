class Student:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
class StudentManager:
    def __init__(self):
        self.items=[]
    def add_student(self,item):
        self.items.append(item)
    def delete_student(self,index):
        del self.items[index-1]
    def display(self):
        for i in range(len(self.items)):
            print("id:"+str(self.items[i].id)+",name:"+self.items[i].name+",age:"+str(self.items[i].age))
    def search(self,id):
        for i in range(len(self.items)):
            if id==self.items[i].id:
                print(self.items[i].name,self.items[i].age)
                break
            else:
                print("查无此人")
    def update(self,id,n,content):
        for i in range(len(self.items)):
            if id==self.items[i].id:
                if n=="name":
                    self.items[i].name=content
                elif n=="age":
                    self.items[i].age = content
                else:
                    print("请重新输入")
                break
            else:
                print("查无此人")
    def insert(self,index,item):
        if index<0 or index>len(self.items):
            print("error")
        self.items.insert(index-1,item)
    def seq_insert(self,item):
        self.items.append(item)
        i=0
        while i<len(self.items):
            c=0
            for j in range(i,len(self.items)):
                if self.items[j].id>c:
                    c=self.items[j].id
                    index=j
            temp=self.items[i]
            self.items[i]=self.items[index]
            self.items[index]=temp
            i=i+1
        self.items.reverse()



#示例用法
a=StudentManager()

s1=Student(1,"a",1)
s2=Student(2,"a",1)
s3=Student(3,"a",1)
s4=Student(4,"a",1)
#添加学生
a.add_student(s1)
a.add_student(s2)
a.add_student(s3)
#清除学生
a.delete_student(3)
#插入学生
a.insert(2,s4)
#display
a.display()
print()
#顺序插入
a.seq_insert(s3)
#display
a.display()
print()
#按学号更新查找信息
a.update(1,"name","s")
a.search(1)
