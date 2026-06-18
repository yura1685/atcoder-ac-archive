from collections import Counter
from math import isqrt

N = int(input())
A = list(map(int,input().split()))
L = Counter(A)

ans = 0
for a in A:
    for d in range(1,isqrt(a)+1):
        if a % d == 0 and L[a]:
            ans += L[d] * L[a//d] * (1 + (d*d != a))

print(ans)