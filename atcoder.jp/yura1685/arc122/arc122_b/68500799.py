from decimal import *

N = int(input())
A = list(map(int,input().split()))
S = sum(A)

def f(x):
    return S + N*x - sum(min(A[i],2*x) for i in range(N))

l, r = 0, 10 ** 10

for _ in range(500):
    m1, m2 = (2*l+r)/3, (l+2*r)/3
    if f(m1) > f(m2):
        l = m1
    else:
        r = m2

print(f(r)/N)