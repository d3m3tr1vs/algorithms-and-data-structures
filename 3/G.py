n=int(input())
l=list(map(int,input().split()))
stack=[]
current=1
for x in l:
    while stack and stack[-1]==current:
        stack.pop()
        current+=1
    if x==current:
        current+=1
    else:
        stack.append(x)

while stack and stack[-1]==current:
    stack.pop()
    current+=1

print("YES" if current == n + 1 else "NO")