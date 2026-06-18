H, W = map(int,input().split())

C = [[0]*(W+1)]+[[0]+list(map(int,input().split())) for _ in range(H)]
A, B = [[0]*(W+1) for _ in range(H+1)], [[0]*(W+1) for _ in range(H+1)]

for h in range(H+1):
    for w in range(W+1):
        if (h+w) % 2 == 0:
            A[h][w] = C[h][w]
        else:
            B[h][w] = C[h][w]
    
black = [[0]*(W+1) for _ in range(H+1)]
white = [[0]*(W+1) for _ in range(H+1)]
for h in range(1,H+1):
    for w in range(1,W+1):
        black[h][w] = black[h-1][w]+black[h][w-1]-black[h-1][w-1]+A[h][w]
        white[h][w] = white[h-1][w]+white[h][w-1]-white[h-1][w-1]+B[h][w]

ans = 0
for h1 in range(1,H+1):
    for w1 in range(1,W+1):
        for h2 in range(h1,H+1):
            for w2 in range(w1,W+1):
                C1 = black[h2][w2]-black[h2][w1-1]-black[h1-1][w2]+black[h1-1][w1-1]
                C2 = white[h2][w2]-white[h2][w1-1]-white[h1-1][w2]+white[h1-1][w1-1]
                if C1 == C2:
                    area = (h2-h1+1) * (w2-w1+1)
                    ans = max(ans,area)
                
print(ans)