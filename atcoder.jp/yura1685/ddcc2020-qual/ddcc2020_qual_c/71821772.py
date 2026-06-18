H, W, K = map(int,input().split())
A = [list(input()) for _ in range(H)]
cnt = 1
for h in range(H):
    for w in range(W):
        if A[h][w] == '.':
            A[h][w] = 0 # type: ignore
        else:
            A[h][w] = cnt # type: ignore
            cnt += 1

for h in range(H):
    for w in range(W-1):
        if A[h][w] and A[h][w+1] == 0:
            A[h][w+1] = A[h][w]

for h in range(H):
    for w in range(W-1,0,-1):
        if A[h][w] and A[h][w-1] == 0:
            A[h][w-1] = A[h][w]

for h in range(H-1):
    for w in range(W):
        if A[h][w] and A[h+1][w] == 0:
            A[h+1][w] = A[h][w]

for h in range(H-1,0,-1):
    for w in range(W):
        if A[h][w] and A[h-1][w] == 0:
            A[h-1][w] = A[h][w]

for a in A:
    print(*a)