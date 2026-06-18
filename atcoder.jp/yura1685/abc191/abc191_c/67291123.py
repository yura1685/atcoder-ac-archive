H, W = map(int,input().split())

g = ['.'+input()+'.' for _ in range(H)]
g = ['.'*(W+2)] + g + ['.'*(W+2)]

ans = 0
for h in range(H+1):
    for w in range(W+1):
        if (g[h][w]+g[h+1][w]+g[h][w+1]+g[h+1][w+1]).count('#') % 2 == 1:
            ans += 1

print(ans)