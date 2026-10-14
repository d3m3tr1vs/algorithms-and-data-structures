def f(x):
    return a*x**3+b*x**2+c*x+d

a,b,c,d=map(int,input().split())
l,r=-10000,10000

if f(l)==0:
    print(l)
elif f(r)==0:
    print(r)
else:
    for _ in range(100):
        m=(l+r)/2
        if f(m)==0:
            break
        if f(l)*f(m)<0:
            r=m
        else:
            l=m

    x=(l+r)/2
    print(f"{x:f}")