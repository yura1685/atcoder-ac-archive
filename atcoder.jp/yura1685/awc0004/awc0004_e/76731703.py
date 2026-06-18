from itertools import accumulate
from collections import defaultdict

N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
S = list(accumulate(A))

ans = 0
d = defaultdict(int)
for s in S:
    ans += d[s - K]
    d[s] += 1

print(ans)