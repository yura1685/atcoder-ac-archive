from bisect import bisect_left, bisect_right
from collections import defaultdict

dh = defaultdict(list)
dw = defaultdict(list)

H, W, hs, ws = map(int,input().split())
N = int(input())
for _ in range(N):
    h, w = map(int,input().split())
    dh[h].append(w)
    dw[w].append(h)

for h in dh.keys():
    dh[h].sort()
for w in dw.keys():
    dw[w].sort()

h, w = hs, ws
Q = int(input())
for _ in range(Q):
    dir, step = input().split()
    step = int(step)
    if dir == 'L':
        ind = bisect_left(dh[h], w)
        if not dh[h] or ind == 0:
            new_w = max(1, w-step)
        else:
            wall = dh[h][ind-1]
            new_w = max(wall+1, w-step)
        w = new_w
    elif dir == 'R':
        ind = bisect_left(dh[h], w)
        if not dh[h] or ind == len(dh[h]):
            new_w = min(W, w+step)
        else:
            wall = dh[h][ind]
            new_w = min(wall-1, w+step)
        w = new_w
    elif dir == 'U':
        ind = bisect_left(dw[w], h)
        if not dw[w] or ind == 0:
            new_h = max(1, h-step)
        else:
            wall = dw[w][ind-1]
            new_h = max(wall+1, h-step)
        h = new_h
    else:
        ind = bisect_left(dw[w], h)
        if not dw[w] or ind == len(dw[w]):
            new_h = min(H, h+step)
        else:
            wall = dw[w][ind]
            new_h = min(wall-1, h+step)
        h = new_h
    print(h, w)