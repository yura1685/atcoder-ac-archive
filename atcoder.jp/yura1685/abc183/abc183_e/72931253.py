H, W = map(int,input().split())
G = ['#'*(W+2)] + ['#'+input()+'#' for _ in range(H)] + ['#'*(W+2)]
mod = 10**9 + 7
ans = [[0]*(W+2) for _ in range(H+2)]
SY = [[0]*(W+2) for _ in range(H+2)]
ST = [[0]*(W+2) for _ in range(H+2)]
SN = [[0]*(W+2) for _ in range(H+2)]
ans[1][1] = SY[1][1] = ST[1][1] = SN[1][1] = 1

for h in range(1,H+1):
    for w in range(1,W+1):
        if h == w == 1:
            continue
        if G[h][w] == '#':
            continue
        ans[h][w] = SY[h][w-1] + ST[h-1][w] + SN[h-1][w-1]
        ans[h][w] %= mod
        SY[h][w] = (SY[h][w-1] + ans[h][w]) % mod
        ST[h][w] = (ST[h-1][w] + ans[h][w]) % mod
        SN[h][w] = (SN[h-1][w-1] + ans[h][w]) % mod

print(ans[-2][-2])