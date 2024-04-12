class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def is_empty(self):
        return self.items == []
    def pop(self):
        self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)

def parreverse(chr):
    b=''
    if chr == ']':
        b='['
    elif chr == ')':
        b="("
    elif chr == '}':
        b="{"
    return b

def parchecker(string):
    stack=Stack()
    for char in string:
        if char == "(" or char=="[" or char=="{":
            stack.push(char)
        elif char == ")" or char=="]" or char=="}":
            if stack.is_empty():
                return(False)
            elif stack.peek() == parreverse(char):
                stack.pop()
            elif stack.peek() != parreverse(char):
                return(False)
    if stack.is_empty():
        return(True)

s=input()
if parchecker(s):
    print("Correct")
else:
    print("Incorrect")