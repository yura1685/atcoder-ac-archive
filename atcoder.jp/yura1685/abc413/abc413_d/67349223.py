from math import gcd
from bisect import *

T = int(input())

def f():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    b1, b2 = 10**10, 10**10
    for aa in A:
        if abs(aa) <= abs(b1):
            b1, b2 = aa, b1
        elif abs(b1) <= abs(aa) <= abs(b2):
            b2 = aa
    g = gcd(b1,b2)
    a, b = b1//g, b2//g # r=b/aと書ける
    if abs(a*b) == 1:
        a = A[0]
        if A.count(a) in [N//2,(N+1)//2,N]:
            return True
        else:
            return False
    p = b1
    for i in range(N-1):
        if (p*b) % a != 0:
            return False
        p = p*b//a
        if bisect(A,p) == bisect_left(A,p):
            return False
    return True

for _ in range(T):
    print('Yes' if f() else 'No')