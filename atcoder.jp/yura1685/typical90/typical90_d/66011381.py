H, W = map(int,input().split())

A = [list(map(int,input().split())) for _ in range(H)]
B = list(zip(*A))
sumh = [sum(h) for h in A]
sumw = [sum(w) for w in B]

C = [[0]*W for _ in range(H)]

for h in range(H):
    for w in range(W):
        C[h][w] = sumh[h] + sumw[w] - A[h][w]

for i in C:
    print(*i)