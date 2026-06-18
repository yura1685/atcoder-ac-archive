N = int(input())
P = [[0] * 1685 for _ in range(1685)]
for _ in range(N):
    a, b, c, d = map(int, input().split())
    c, d = c-1, d-1
    P[a][b] += 1
    P[c+1][b] -= 1
    P[a][d+1] -= 1
    P[c+1][d+1] += 1

for h in range(1685):
    for w in range(1684):
        P[h][w+1] += P[h][w]
for w in range(1685):
    for h in range(1684):
        P[h+1][w] += P[h][w]

ans = 0
for h in range(1685):
    for w in range(1685):
        if P[h][w]:
            ans += 1

print(ans)