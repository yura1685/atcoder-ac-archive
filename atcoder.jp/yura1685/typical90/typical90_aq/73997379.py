from collections import deque

I = input().split()
H, W = int(I[0]), int(I[1])
I = input().split()
sh, sw = int(I[0]), int(I[1])
I = input().split()
gh, gw = int(I[0]), int(I[1])
sh, sw, gh, gw = sh-1, sw-1, gh-1, gw-1
c:list[tuple[int, int]] = [(-1, 0), (0, -1), (0, 1), (1, 0)]
S:list[str] = [input() for _ in range(H)]
cnt:list[list[list[int]]] = [[[1 << 30] * 4 for _ in range(W)] for _ in range(H)]

dq = deque([(sh, sw, 0, 4)])
while dq:
    h, w, turn, dir = dq.popleft()
    if dir < 4 and turn > cnt[h][w][dir]:
        continue
    if h == gh and w == gw:
        continue

    for dh, dw in c:
        nh, nw = h + dh, w + dw
        if not (0 <= nh < H and 0 <= nw < W) or S[nh][nw] == '#':
            continue
        if nh < h:   ndir = 0
        elif nh > h: ndir = 2
        elif nw < w: ndir = 3
        else:        ndir = 1
        cost = 0 if (dir == 4 or dir == ndir) else 1
        new_turn = turn + cost
    
        if cnt[nh][nw][ndir] > new_turn:
            cnt[nh][nw][ndir] = new_turn
            if cost == 0:
                dq.appendleft((nh, nw, new_turn, ndir))
            else:
                dq.append((nh, nw, new_turn, ndir))

print(min(cnt[gh][gw]))