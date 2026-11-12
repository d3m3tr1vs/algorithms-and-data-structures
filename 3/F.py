import collections
n,k=map(int,input().split())
l=list(map(int,input().split()))
dq=collections.deque()
res=[]
for i in range(n):
    if i>=k and dq[0]==i-k:
        dq.popleft()
    while len(dq)>0 and l[dq[-1]]>=l[i]:
        dq.pop()
    dq.append(i)
    if i>=k-1:
        res.append(l[dq[0]])
print(*res,sep='\n')