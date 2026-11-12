class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        return 'error'
    def front(self):
        if not self.is_empty():
            return self.items[0]
        return 'error'
    def size(self):
        return len(self.items)
    def clear(self):
        self.items=[]

queue=Queue()
running=True
while running:
    s=input().split()
    if s[0]=='push':
        queue.push(int(s[1]))
        print('ok')
    elif s[0]=='pop':
        print(queue.pop())
    elif s[0]=='front':
        print(queue.front())
    elif s[0]=='size':
        print(queue.size())
    elif s[0]=='clear':
        queue.clear()
        print('ok')
    elif s[0]=='exit':
        running=False
print('bye')