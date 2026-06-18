from heapq import *

N, M, X = map(int, input().split())
GT = [[] for _ in range(N)]
GF = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    GT[u-1].append(v-1)
    GF[v-1].append(u-1)
    
inf = 10 ** 18
dp = [[inf, inf] for _ in range(N)]
dp[0][0] = 0

hq = []
heappush(hq, (0, 0, 0))
while hq:
    dist, u, dir = heappop(hq)
    if dir == 0:
        for v in GT[u]:
            if dp[u][0] + 1 < dp[v][0]:
                dp[v][0] = dp[u][0] + 1
                heappush(hq, (dist + 1, v, 0))
        if dp[u][0] + X < dp[u][1]:
            dp[u][1] = dp[u][0] + X
            heappush(hq, (dist + X, u, 1))
    else:
        for v in GF[u]:
            if dp[u][1] + 1 < dp[v][1]:
                dp[v][1] = dp[u][1] + 1
                heappush(hq, (dist + 1, v, 1))
        if dp[u][1] + X < dp[u][0]:
            dp[u][0] = dp[u][1] + X
            heappush(hq, (dist + X, u, 0))

print(min(dp[N-1]))