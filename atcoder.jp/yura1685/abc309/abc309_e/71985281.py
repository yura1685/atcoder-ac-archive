from collections import deque

N, M = map(int,input().split())
P = [int(x)-1 for x in input().split()]
g = [[] for _ in range(N)]
for i in range(N-1):
    g[P[i]].append(i+1)

dp = [0] * N
for _ in range(M):
    x, y = map(int,input().split())
    dp[x-1] = max(dp[x-1], y+1)

dq = deque([(0, dp[0])])
while dq:
    u, l = dq.popleft()
    for v in g[u]:
        dp[v] = max(l-1, dp[v])
        dq.append((v, dp[v]))

print(sum([1 if dp[u] else 0 for u in range(N)]))