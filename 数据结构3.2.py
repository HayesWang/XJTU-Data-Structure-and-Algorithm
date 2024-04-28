# 基于单链表，编写一个通讯录管理程序，实现以下功能：
# 1.每个联系人的信息包含姓名、电话；
# 2.可以插入新的联系人信息
# 3.可以根据姓名删除联系人信息；
# 4.可以显示通讯录中联系人信息。


class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Contact:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, name, phone):
        person = Person(name, phone)
        person.next = self.head
        self.head = person

    def remove(self, name):
        pre = None
        cur = self.head
        while cur and cur.name != name:
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
            print(cur.name, cur.phone)
            cur = cur.next

    def insert(self, pos, name, phone):
        if pos <= 0:
            self.add(name, phone)
        else:
            person = Person(name, phone)
            pre = self.head
            count = 0
            while count < pos - 1 and pre:
                pre = pre.next
                count += 1
            if not pre:
                raise IndexError("Index out of range")
            person.next = pre.next
            pre.next = person

contact = Contact()
#Three different contacts
contact.add("Tom", "123456")
contact.add("Jerry", "654321")
contact.add("Jack", "987654")
print("All contacts:")
#Display all contacts
contact.display()
#Insert a new contact
contact.insert(2, "Rose", "456789")
print("Insert Rose at 2:")
contact.display()
#Remove a contact
contact.remove("Jerry")
print("Remove Jerry:")
contact.display()


