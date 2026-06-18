from collections import defaultdict, deque
from bisect import bisect

H, W, N = map(int,input().split())

row_obs = defaultdict(list)
col_obs = defaultdict(list)

sx, sy = map(int,input().split())
gx, gy = map(int,input().split())
for _ in range(N):
    x, y = map(int,input().split())
    row_obs[x].append(y)
    col_obs[y].append(x)

for r in row_obs:
    row_obs[r].sort()
for c in col_obs:
    col_obs[c].sort()

dq = deque([(sx, sy)])
dist = {(sx,sy): 0}

while dq:
    x, y = dq.popleft()
    d = dist[(x,y)]
    if (x, y) == (gx, gy):
        exit(print(d))
    
    if x in row_obs:
        idx = bisect(row_obs[x], y)
        if idx > 0:
            y_left = row_obs[x][idx-1] + 1
            if (x, y_left) not in dist:
                dist[(x, y_left)] = d + 1
                dq.append((x, y_left))
        if idx < len(row_obs[x]):
            y_right = row_obs[x][idx] - 1
            if (x, y_right) not in dist:
                dist[(x, y_right)] = d + 1
                dq.append((x, y_right))
    
    if y in col_obs:
        idx = bisect(col_obs[y], x)
        if idx > 0:
            x_upper = col_obs[y][idx-1] + 1
            if (x_upper, y) not in dist:
                dist[(x_upper, y)] = d + 1
                dq.append((x_upper, y))
        if idx < len(col_obs[y]):
            x_lower = col_obs[y][idx] - 1
            if (x_lower, y) not in dist:
                dist[(x_lower, y)] = d + 1
                dq.append((x_lower, y))

print(-1)