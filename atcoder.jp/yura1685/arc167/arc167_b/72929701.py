from collections import defaultdict
from math import isqrt
mod = 998244353

A, B = map(int,input().split())
d = defaultdict(int)
for n in range(2, isqrt(A) + 1):
    while A % n == 0:
        A //= n
        d[n] += 1
if A > 1:
    d[A] += 1

M = 1

for p, e in d.items():
    M *= (e*B+1)

if M % 2 == 0:
    print((B*M//2) % mod)

else:
    print((B*(M//2)+B//2) % mod)