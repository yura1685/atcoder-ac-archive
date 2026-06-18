from heapq import heappop, heappush

N, M = map(int,input().split())

g = [[], []] + [[(i+1,0)] for i in range(N-1)]

for _ in range(M):
    L, R, C = map(int,input().split())
    g[L].append((R,C))

S = []
heappush(S,(0,1))
c = [0] * (N+1)
inf = 10**18
ans = [inf for _ in range(N+1)]
while S:
    s, u = heappop(S)
    if c[u] == 1:
        continue
    for v, w in g[u]:
        heappush(S,(s+w, v))
    c[u] = 1
    ans[u] = min(ans[u],s)

print(ans[-1] if ans[-1] < inf else -1)