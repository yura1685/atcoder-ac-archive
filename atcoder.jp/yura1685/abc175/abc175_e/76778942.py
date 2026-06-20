I = input().split()
H, W, K = int(I[0]), int(I[1]), int(I[2])
A = [[0] * W for _ in range(H)]
for _ in range(K):
    I = input().split()
    h, w, v = int(I[0]), int(I[1]), int(I[2])
    A[h-1][w-1] = v

S = [[[0] * 4 for _ in range(W)] for _ in range(H)]
for h in range(H):
    for w in range(W):
        if h == 0:
            if w == 0:
                S[h][w][1] = A[h][w]
            else:
                for i in range(1, 4):
                    S[h][w][i] = max(S[h][w-1][i-1] + A[h][w], S[h][w-1][i])
        else:
            if w == 0:
                S[h][w][0] = max(S[h-1][w])
                S[h][w][1] = S[h][w][0] + A[h][w]
            else:
                S[h][w][0] = max(S[h][w-1][0], max(S[h-1][w]))
                S[h][w][1] = max(S[h][w-1][1], S[h][w-1][0] + A[h][w], max(S[h-1][w]) + A[h][w])
                for i in range(2, 4):
                    S[h][w][i] = max(S[h][w-1][i-1] + A[h][w], S[h][w-1][i])

print(max(S[H-1][W-1]))