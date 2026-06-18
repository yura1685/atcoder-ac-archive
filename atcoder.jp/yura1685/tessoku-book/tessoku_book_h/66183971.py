H, W = map(int,input().split())
glid = [list(map(int,input().split())) for _ in range(H)]
S = [[0]*(W+1) for _ in range(H+1)]
S[1][1] = glid[0][0]
for w in range(1,W):
    S[1][w+1] = S[1][w] + glid[0][w]
for h in range(1,H):
    S[h+1][1] = S[h][1] + glid[h][0]

for h in range(1,H):
    for w in range(1,W):
        S[h+1][w+1] = S[h][w+1] + S[h+1][w] - S[h][w] + glid[h][w]

Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int,input().split())
    n = S[c][d] - S[c][b-1] - S[a-1][d] + S[a-1][b-1]
    print(n)