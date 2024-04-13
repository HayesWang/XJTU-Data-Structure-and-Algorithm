class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty:
            return self.items.pop(0)
        else:
            return ("error")
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)

q=Queue()
q.enqueue(22)
q.enqueue(33)
print(q.dequeue())