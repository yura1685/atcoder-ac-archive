from collections import deque

H, W = map(int,input().split())
S = [list(input()) for _ in range(H)]
c = [(-1,0),(0,-1),(0,1),(1,0)]

for h in range(H):
    for w in range(W):
        if S[h][w] != '#':
            continue
        for dh, dw in c:
            nh, nw = h+dh, w+dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.':
                S[nh][nw] = 'M'

res = []

cnt = 0
for h in range(H):
    for w in range(W):
        if S[h][w] != '.':
            continue
        s = set()
        ans = 0        
        S[h][w] = cnt
        d = deque([(h,w)])
        while d:
            ans += 1
            x, y = d.popleft()
            for dx, dy in c:
                nx, ny = x+dx, y+dy
                if 0 <= nx < H and 0 <= ny < W:
                    if S[nx][ny] == '.':
                        S[nx][ny] = cnt
                        d.append((nx,ny))
                    elif S[nx][ny] == 'M':
                        s.add((nx,ny))
        res.append(ans + len(s))
        cnt += 1

print(max(res) if cnt else 1) 