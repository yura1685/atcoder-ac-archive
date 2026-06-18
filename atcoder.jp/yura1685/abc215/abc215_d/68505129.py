from collections import defaultdict
from math import isqrt

N, M = map(int,input().split())
A = list(map(int,input().split()))

ma = max(A)
prime = [False, False] + [True] * ma
for p in range(2,ma+1):
    if not prime[p]:
        continue
    for i in range(2*p,ma+2,p):
        prime[i] = False

d = defaultdict(int)

for a in A:
    for p in range(2,isqrt(a)+1):
        if not prime[p]:
            continue
        while a % p == 0:
            a //= p
            d[p] = 1
        if a == 1:
            break
    if a > 1:
        d[a] = 1

ans = [False] + [True] * M
for p in d.keys():
    for i in range(p,M+1,p):
        ans[i] = False

print(sum(ans))
for i in range(M+1):
    if ans[i]:
        print(i)