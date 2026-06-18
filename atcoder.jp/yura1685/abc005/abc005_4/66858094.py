N = int(input())
D = [[0]*(N+1)] + [[0]+list(map(int,input().split())) for _ in range(N)]

yum = [[0]*(N+1) for _ in range(N+1)]
for h in range(1,N+1):
    for w in range(1,N+1):
        yum[h][w] = yum[h-1][w] + yum[h][w-1] - yum[h-1][w-1] + D[h][w]

c = [0]*(N*N+1)

for ax in range(1,N+1):
    for ay in range(1,N+1):
        for bx in range(ax,N+1):
            for by in range(ay,N+1):
                aji = yum[bx][by]-yum[bx][ay-1]-yum[ax-1][by]+yum[ax-1][ay-1]
                area = (bx-ax+1)*(by-ay+1)
                c[area] = max(c[area],aji)

for i in range(1,N*N+1):
    c[i] = max(c[i-1],c[i])

Q = int(input())
for _ in range(Q):
    P = int(input())
    print(c[P])