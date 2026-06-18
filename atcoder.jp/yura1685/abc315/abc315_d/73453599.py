from collections import defaultdict

H, W = map(int,input().split())
C = [[ord(x)-96 for x in input()] for _ in range(H)]

dx = [defaultdict(int) for _ in range(H)]
dy = [defaultdict(int) for _ in range(W)]

for h in range(H):
    for w in range(W):
        dx[h][C[h][w]] += 1
        dy[w][C[h][w]] += 1

while True:
    nexh, nexw = [], []
    for h in range(H):
        if len(dx[h]) == 1 and max(dx[h].values()) >= 2:
            nexh.append(h)
    for w in range(W):
        if len(dy[w]) == 1 and max(dy[w].values()) >= 2:
            nexw.append(w)

    if nexh or nexw:
        for h in nexh:
            col = next(iter(dx[h]))
            dx[h].clear()
            for w in range(W):
                if col in dy[w]:
                    dy[w][col] -= 1
                    if not dy[w][col]:
                        del dy[w][col]
        for w in nexw:
            if not dy[w]: continue
            col = next(iter(dy[w]))
            dy[w].clear()
            for h in range(H):
                if col in dx[h]:
                    dx[h][col] -= 1
                    if not dx[h][col]:
                        del dx[h][col]
    else:
        break

print(sum(sum(d.values()) for d in dx))