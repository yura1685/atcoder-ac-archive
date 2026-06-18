H, W, D = map(int,input().split())
N = H*W
A = [[int(x) for x in input().split()] for _ in range(H)]
I = [(-1,-1) for _ in range(N+1)]
for i in range(H):
    for j in range(W):
        I[A[i][j]] = (i,j)

dist = [0] * (N+1-D)
for i in range(1,N+1-D):
    dist[i] = abs(I[i][0] - I[i+D][0]) + abs(I[i][1] - I[i+D][1])

ac = dist.copy()
for i in range(D,N+1-D):
    ac[i] += ac[i-D]

Q = int(input())
for _ in range(Q):
    l, r = map(int,input().split())
    if l == r:
        print(0)
    elif r - l == D:
        print(dist[l])
    else:
        if l - D >= 1:
            print(ac[r-D] - ac[l-D])
        else:
            print(ac[r-D])