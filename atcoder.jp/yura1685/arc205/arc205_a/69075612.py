N, Q = map(int,input().split())
S = [input() for _ in range(N)]

T = [[0]*N for _ in range(N)]

for h in range(N-1):
    for w in range(N-1):
        if S[h][w] == S[h+1][w] == S[h][w+1] == S[h+1][w+1] == '.':
            T[h+1][w+1] = 1
    
U = [[0]*N for _ in range(N)]
for i in range(1,N):
    for j in range(1,N):
        U[i][j] = T[i][j] + U[i-1][j] + U[i][j-1] - U[i-1][j-1]

for _ in range(Q):
    u, d, l, r = map(int,input().split())
    d, r = d-1, r-1
    print(U[d][r]-U[d][l-1]-U[u-1][r]+U[u-1][l-1])