class Stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "error"
        return self.items.pop()

    def back(self):
        if self.is_empty():
            return "error"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items=[]


stack=Stack()
running=True
while running:
    s=input().split()
    if s[0]=='push':
        stack.push(int(s[1]))
        print('ok')
    elif s[0]=='pop':
        print(stack.pop())
    elif s[0]=='back':
        print(stack.back())
    elif s[0]=='size':
        print(stack.size())
    elif s[0]=='clear':
        stack.clear()
        print('ok')
    elif s[0]=='exit':
        running=False
print('bye')