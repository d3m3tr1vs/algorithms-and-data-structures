def binary_search(arr,x):
    l = 0
    r = len(arr)-1
    while l<=r:
        m = (r + l) // 2
        if arr[m] == x:
            return 'YES'
        elif arr[m] < x:
            l = m+1
        else:
            r = m-1
    return 'NO'
n,k=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
#print(n,k,l1,l2)
for x in l2:
    print(binary_search(l1,x))