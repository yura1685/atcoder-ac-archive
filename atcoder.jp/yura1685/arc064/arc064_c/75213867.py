import heapq

sx, sy, gx, gy = map(int, input().split())
N = int(input())
Ba = []
for _ in range(N):
    x, y, r = map(int, input().split())
    Ba.append((x, y, r))
Ba = [(sx, sy, 0)] + Ba + [(gx, gy, 0)]

inf = 10 ** 12
G = [[inf] * (N+2) for _ in range(N+2)]
for i in range(N+2):
    G[i][i] = 0

def dist(xi, yi, ri, xj, yj, rj):
    return max(((xi-xj)**2 + (yi-yj)**2)**(1/2)-ri-rj, 0)

for i in range(N+2):
    for j in range(i+1, N+2):
        xi, yi, ri = Ba[i]
        xj, yj, rj = Ba[j]
        G[i][j] = G[j][i] = dist(xi, yi, ri, xj, yj, rj)

ans = [inf] * (N+2)
ans[0] = 0
hq = []
heapq.heappush(hq, (0, 0))
while hq:
    d, u = heapq.heappop(hq)
    if d > ans[u]:
        continue

    for v in range(N+2):
        if ans[v] > ans[u] + G[u][v]:
            ans[v] = ans[u] + G[u][v]
            heapq.heappush(hq, (ans[v], v))

print(ans[-1])