from itertools import accumulate
from bisect import bisect_left

N, K = map(int,input().split())
a = list(map(int,input().split()))
S = [0] + list(accumulate(a))

ans = 0
for i in range(1,N+1):
    a = bisect_left(S,K+S[i-1])
    ans += N-a+1

print(ans)