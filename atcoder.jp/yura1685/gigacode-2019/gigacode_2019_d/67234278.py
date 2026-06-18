H, W, K, V = map(int,input().split())

A = [[0]*(W+1)]
for _ in range(H):
    A.append([0]+list(map(int,input().split())))

P = [[0]*(W+1) for _ in range(H+1)]
for h in range(1,H+1):
    for w in range(1,W+1):
        P[h][w] = P[h-1][w] + P[h][w-1] - P[h-1][w-1] + A[h][w]

ans = 0
for h1 in range(1,H+1):
    for w1 in range(1,W+1):
        for h2 in range(h1,H+1):
            for w2 in range(w1,W+1):
                house = P[h2][w2]-P[h2][w1-1]-P[h1-1][w2]+P[h1-1][w1-1]
                tika  = (h2-h1+1) * (w2-w1+1) * K
                if house + tika <= V:
                    ans = max(ans,tika//K)

print(ans)