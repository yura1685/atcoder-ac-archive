H, W = map(int,input().split())
S = [input() for _ in range(H)]

# Orb[i][j] = S[i][j] より右にある O の個数
# Ing[i][j] = S[i][j] より下にある I の個数
Orb = [[0]*W for _ in range(H)]
Ing = [[0]*W for _ in range(H)]

for h in range(H):
    for w in range(W):
        if S[h][w] == 'O':
            Orb[h][w] = 1
        if S[h][w] == 'I':
            Ing[h][w] = 1

for h in range(H):
    for w in range(W-2,-1,-1):
        Orb[h][w] += Orb[h][w+1]

for h in range(H-2,-1,-1):
    for w in range(W):
        Ing[h][w] += Ing[h+1][w]

ans = 0
for h in range(H):
    for w in range(W):
        if S[h][w] == 'J':
            ans += Orb[h][w] * Ing[h][w]

print(ans)