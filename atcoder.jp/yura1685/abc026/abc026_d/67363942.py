from math import sin, pi

A, B, C = map(int,input().split())

def f(x):
    return A*x + B*sin(C*x*pi)

l, r = 0, 102
while abs(f(l)-100) > 10**(-8):
    mid = (l+r)/2
    if f(mid) > 100:
        r = mid
    else:
        l = mid
print(r)