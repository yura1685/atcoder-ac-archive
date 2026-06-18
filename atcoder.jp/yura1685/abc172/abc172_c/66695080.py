from itertools import accumulate
from bisect import bisect

N, M, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = list(map(int, input().split()))

Sa = list(accumulate(A))
Sb = list(accumulate(B))

ans = 0
for i in range(N+1):
    a = Sa[i]
    if a > K:
        break
    b = bisect(Sb,K-a)
    ans = max(ans,b+i)

print(ans)