N, M, Q = map(int,input().split())

glid = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    L, R = map(int,input().split())
    glid[L][R] += 1

for h in range(1,N+1):
    for w in range(1,N+1):
        glid[h][w] += glid[h][w-1]

for w in range(1,N+1):
    for h in range(N-1,-1,-1):
        glid[h][w] += glid[h+1][w]

for _ in range(Q):
    p, q = map(int,input().split())
    print(glid[p][q])