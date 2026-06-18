N, A, B = map(int, input().split())
g = [[0] * N for _ in range(N)]
for _ in range(A):
    h1, w1, h2, w2 = map(lambda x: int(x)-1, input().split())
    for h in range(h1, h2+1):
        for w in range(w1, w2+1):
            if g[h][w] == 0:
                g[h][w] = 1
ans = 0
for _ in range(B):
    h1, w1, h2, w2 = map(lambda x: int(x)-1, input().split())
    for h in range(h1, h2+1):
        for w in range(w1, w2+1):
            if g[h][w] == 1:
                g[h][w] = 2
                ans += 1
print(ans)