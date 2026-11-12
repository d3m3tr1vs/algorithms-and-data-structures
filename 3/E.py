class Deque:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push_front(self, item):
        self.items=[item]+self.items
    def push_back(self, item):
        self.items.append(item)
    def pop_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        return 'error'
    def pop_back(self):
        if not self.is_empty():
            return self.items.pop()
        return 'error'
    def front(self):
        if not self.is_empty():
            return self.items[0]
        return 'error'
    def back(self):
        if not self.is_empty():
            return self.items[-1]
        return 'error'
    def size(self):
        return len(self.items)
    def clear(self):
        self.items=[]

deque=Deque()
running=True
while running:
    s=input().split()
    if s[0]=='push_front':
        deque.push_front(int(s[1]))
        print('ok')
    elif s[0]=='push_back':
        deque.push_back(int(s[1]))
        print('ok')
    elif s[0]=='pop_front':
        print(deque.pop_front())
    elif s[0]=='pop_back':
        print(deque.pop_back())
    elif s[0]=='front':
        print(deque.front())
    elif s[0]=='back':
        print(deque.back())
    elif s[0]=='size':
        print(deque.size())
    elif s[0]=='clear':
        deque.clear()
        print('ok')
    elif s[0]=='exit':
        running=False
print('bye')