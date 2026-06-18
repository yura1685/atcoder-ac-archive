D, N = map(int,input().split())
temp = [int(input()) for _ in range(D)]
clot = [tuple(map(int,input().split())) for _ in range(N)]
v = [c for a,b,c in clot]
dp = [[-10**6]*N for _ in range(D)]

for i in range(D):
    t = temp[i]
    for j in range(N):
        a, b, c = clot[j]
        if a <= t <= b:
            dp[i][j] = 0

for h in range(1,D):
    for w in range(N):
        if dp[h][w] == 0:
            dp[h][w] = max([dp[h-1][w2] + abs(v[w]-v[w2]) for w2 in range(N)])

print(max(dp[-1]))