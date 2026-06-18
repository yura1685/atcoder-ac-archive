from math import isqrt
from itertools import accumulate

N = int(input())

rN = isqrt(N)//3
prime = [False,False] + [True]*(rN)
for p in range(2,rN):
    if not prime[p]:
        continue
    for i in range(2*p,rN+2,p):
        prime[i] = False

p_ac = list(accumulate(prime))

ans = 0
for a in range(2,N):
    if a**5 >= N:
        break
    if not prime[a]:
        continue
    for b in range(a+1,N):
        if a*a*b**3 >= N:
            break
        if not prime[b]:
            continue
        cM = isqrt(N//(a*a*b))
        ans += max(p_ac[cM] - p_ac[b], 0)

print(ans)