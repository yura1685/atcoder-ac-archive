from bisect import bisect
from functools import cmp_to_key

def solve(A:list) -> int:
    INF = 10**10

    dp = [INF]*(N+1)
    dp[0] = -1
    for a in A:
        idx = bisect(dp, a-1)
        dp[idx] = min(a, dp[idx])
    return max(i for i in range(N+1) if dp[i] < INF)

def compare(a, b):
    if a[0] < b[0]:
        return -1
    if a[0] > b[0]:
        return 1
    if a[1] > b[1]:
        return -1
    if a[1] < b[1]:
        return 1

N = int(input())
tako = set()
for _ in range(N):
    A, B = map(int, input().split())
    tako.add((A, B))
tako = list(tako)
tako.sort(key=cmp_to_key(compare))
X = [t[1] for t in tako]
print(solve(X))