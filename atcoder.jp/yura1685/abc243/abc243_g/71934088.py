from math import isqrt
from itertools import accumulate

def solve():
    X = int(input())
    X2 = isqrt(X)
    X4 = isqrt(X2)
    X8 = isqrt(X4)
    L2 = [0] * (X4+1000)
    for i in range(1,X4+1000):
        L2[i] = max(X2-i*i+1,0)
    L2AC = list(accumulate(L2))
    L3 = [0] * (X8+2)
    for i in range(1,X8+2):
        j = i*i
        L3[i] = L2AC[-1] - L2AC[j-1]
    for u in range(X8+1,0,-1):
        for v in range(1,isqrt(u)+1):
            L3[v] += L3[u]
    print(L3[1]//2)

T = int(input())
for _ in range(T):
    solve()