N = int(input())
P = []
for _ in range(N):
    x, y = map(int,input().split())
    P.append((x,-y))
P.sort()
Y = [-P[i][1] for i in range(N)]

from bisect import bisect

def solve(N, A):
    INF = 10**10

    dp = [INF]*(N+1)
    dp[0] = -1
    for a in A:
        idx = bisect(dp, a-1)
        dp[idx] = min(a, dp[idx])
    return max(i for i in range(N+1) if dp[i] < INF)

print(solve(N, Y))