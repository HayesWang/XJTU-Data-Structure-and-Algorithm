class Stack:
    def __init__(self):
        self.items = []
    #入栈
    def push(self,item):
        self.items.append(item)
    #判断为空？
    def is_empty(self):
        return self.items == []
    #出栈
    def pop(self):
        self.items.pop()
    #观察
    def peek(self):
        return self.items[-1]
    #栈元素数量
    def size(self):
        return len(self.items)

#括号反转方法
def parreverse(chr):
    b=''
    if chr == ']':
        b='['
    elif chr == ')':
        b="("
    elif chr == '}':
        b="{"
    return b

#括号检查方法
def parchecker(string):
    stack=Stack()
    for char in string:
        #左括号入栈
        if char == "(" or char=="[" or char=="{":
            stack.push(char)
        elif char == ")" or char=="]" or char=="}":
        #右括号判断是否空栈，是否和栈顶括号互补
            if stack.is_empty():
                return(False)
            elif stack.peek() == parreverse(char):
                stack.pop()
            elif stack.peek() != parreverse(char):
                return(False)
    #遍历完后判断是否空栈（是否完成一一互补）
    if stack.is_empty():
        return(True)

s=input()
if parchecker(s):
    print("Correct")
else:
    print("Incorrect")