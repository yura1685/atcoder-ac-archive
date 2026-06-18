from collections import deque

H, W, T = map(int,input().split())
A = [input() for _ in range(H)]
candy = []
for i in range(H):
    for j in range(W):
        if A[i][j] == 'o':
            candy.append((i,j))
        elif A[i][j] == 'S':
            sx, sy = i, j
        elif A[i][j] == 'G':
            gx, gy = i, j
candy = [(sx,sy)] + candy + [(gx,gy)]

N = len(candy)
inf = float('inf')
dist = [[inf]*N for _ in range(N)]
c = [(-1,0),(0,-1),(0,1),(1,0)]

def bfs(s):
    x, y = candy[s]
    d = deque([(x,y)])
    step = [[inf]*W for _ in range(H)]
    check = [[0]*W for _ in range(H)]
    step[x][y] = 0
    check[x][y] = 1
    while d:
        x, y = d.popleft()
        for dx, dy in c:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and A[nx][ny] != '#' and check[nx][ny] == 0:
                check[nx][ny] = 1
                step[nx][ny] = step[x][y] + 1
                d.append((nx,ny))
    for g in range(N):
        dist[s][g] = step[candy[g][0]][candy[g][1]]

for i in range(N): bfs(i)

dp = [[inf]*N for _ in range(1 << N)]
dp[1][0] = 0

for mask in range(1 << N):
    for u in range(N):
        if dp[mask][u] == inf:
            continue
        for v in range(N):
            if (mask >> v) & 1:
                continue
            new_mask = mask | (1 << v)
            dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + dist[u][v])

ans = -1
for mask in range(1 << N):
    if dp[mask][-1] > T:
        continue
    ans = max(ans, mask.bit_count()-2)

print(ans)