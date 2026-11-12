from collections import deque

n=int(input())
l=deque()
r=deque()
res=[]
for j in range(n):
    s=input().split()
    if s[0]=='+':
        i=int(s[1])
        r.append(i)
        if len(l)<len(r):
            l.append(r.popleft())
    elif s[0]=='*':
        i=int(s[1])
        l.append(i)
        if len(l)>len(r)+1:
            r.appendleft(l.pop())
    elif s[0]=='-':
        #print(l.popleft())
        res.append(str(l.popleft()))
        if len(l)<len(r):
            l.append(r.popleft())

print("\n".join(res))