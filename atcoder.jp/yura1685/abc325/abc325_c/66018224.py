from collections import deque

H, W = map(int, input().split())

S = [list('.'+input()+'.') for _ in range(H)]
S = [['.']*(W + 2)]+S+[['.']*(W + 2)]

C = [(-1,-1), (-1,0), (-1,1),
     ( 0,-1), ( 0,1),
     ( 1,-1), ( 1,0), ( 1,1)]

sensor = 0
for h in range(1, H + 1):
    for w in range(1, W + 1):
        if S[h][w] == '#':
            sensor += 1
            d = deque()
            d.append((h, w))
            S[h][w] = '.'
            while d:
                i, j = d.popleft()
                for dh, dw in C:
                    ni, nj = i + dh, j + dw
                    if S[ni][nj] == '#':
                        S[ni][nj] = '.'
                        d.append((ni, nj))

print(sensor)
