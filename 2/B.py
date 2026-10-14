def binary_search(arr,x):
    l = -1
    r = len(arr)
    while r - l > 1:
        m = (r + l) // 2
        if arr[m] <= x:
            l = m
        else:
            r = m
    if l == -1:
        return arr[0]
    if r == len(arr):
        return arr[-1]
    if abs(arr[l] - x) <= abs(arr[r] - x):
        return arr[l]
    else:
        return arr[r]

n,k=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
#print(n,k,l1,l2)
for x in l2:
    print(binary_search(l1,x))