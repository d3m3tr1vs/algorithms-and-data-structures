#x^2+sqrt(x)-c=0    x - ?
def f(x,c):
    return x**2+x**.5-c
c=float(input())
l,r=0,c**.5
while True:
    m=(l+r)/2
    if m<=l or m>=r:
        break
    if f(m,c)<0:
        l=m
    else:
        r=m
print(m)
