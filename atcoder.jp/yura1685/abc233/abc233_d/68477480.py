from itertools import accumulate
from collections import defaultdict

N, K = map(int,input().split())
A = [0] + list(map(int,input().split()))
B = list(accumulate(A))
d = defaultdict(int)

ans = 0
for i in range(N+1):
    ans += d[B[i]-K]
    d[B[i]] += 1
print(ans)