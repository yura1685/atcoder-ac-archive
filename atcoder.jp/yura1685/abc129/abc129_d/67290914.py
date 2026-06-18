from bisect import bisect

H, W = map(int,input().split())
g = ['#'+input()+'#' for _ in range(H)]
g = ['#'*(W+2)] + g + ['#'*(W+2)]

wally, wallt = [[] for _ in range(H+2)], [[] for _ in range(W+2)]
for h in range(H+2):
    for w in range(W+2):
        if g[h][w] == '#':
            wally[h].append(w)
            wallt[w].append(h)

ans = 0
for h in range(1,H+1):
    for w in range(1,W+1):
        if g[h][w] == '#':
            continue
        y = bisect(wally[h],w)
        t = bisect(wallt[w],h)
        ans = max(ans,wally[h][y]-wally[h][y-1]+wallt[w][t]-wallt[w][t-1]-3)

print(ans)