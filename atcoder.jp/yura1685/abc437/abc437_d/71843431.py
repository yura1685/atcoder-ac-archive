from itertools import accumulate
from bisect import bisect
N, M = map(int,input().split())
A = list(map(int,input().split()))
B = sorted(map(int,input().split()))
SB = [0] + list(accumulate(B))
mod = 998244353

ans = 0
for a in A:
    k = bisect(B,a)
    ans += k*a - SB[k]
    ans += SB[M] - SB[k] - (M-k)*a
    ans %= mod

print(ans)