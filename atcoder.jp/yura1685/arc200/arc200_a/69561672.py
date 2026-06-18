from math import gcd
from collections import defaultdict

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    d = defaultdict(list)
    for i in range(N):
        a, b = A[i], B[i]
        g = gcd(a,b)
        a, b = a//g, b//g
        d[(a,b)].append(i)
    if len(d.keys()) == 1:
        print('No')
        return
    for key in d.keys():
        try:
            x = x
            try:
                y = y
            except NameError:
                y = d[key][0]
                break
        except NameError:
            x = d[key][0]
    X = [0] * N
    X[x] = A[y] + B[y]
    X[y] = A[x] + B[x]
    if A[x]/B[x] < A[y]/B[y]:
        X[x] *= -1
    else:
        X[y] *= -1
    print('Yes')
    print(*X)

T = int(input())
for _ in range(T):
    solve()