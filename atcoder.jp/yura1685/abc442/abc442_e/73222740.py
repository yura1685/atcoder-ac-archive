from functools import cmp_to_key
from math import gcd
from collections import defaultdict

def cmp(a, b):
    if a[0] > 0 or (a[0] == 0 and a[1] > 0):
        if b[0] < 0 or (b[0] == 0 and b[1] < 0):
            return -1
    if a[0] < 0 or (a[0] == 0 and a[1] < 0):
        if b[0] > 0 or (b[0] == 0 and b[1] > 0):
            return 1
    if a[0] == 0:
        if a[1] > 0:
            if b[0] == 0:
                if b[1] > 0:
                    return 0
            else:
                return -1
        else:
            if b[0] == 0:
                if b[1] < 0:
                    return 0
            else:
                return -1
    c = a[0] * b[1] - a[1] * b[0]
    if c == 0:
        return 0
    else:
        if c > 0:
            return 1
        else:
            return -1

N, Q = map(int,input().split())
P = []
for i in range(N):
    x, y = map(int,input().split())
    g = gcd(x, y)
    x //= g
    y //= g
    P.append((x,y))

S = sorted(P, key=cmp_to_key(cmp))
L = defaultdict(int)
R = defaultdict(int)
for i in range(N):
    if L[S[i]] == 0:
        L[S[i]] = i + 1
    R[S[i]] = i + 1

for _ in range(Q):
    A, B = map(int,input().split())
    A, B = A-1, B-1
    print((R[P[B]] - L[P[A]]) % N + 1)