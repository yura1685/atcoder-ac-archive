H, W, C = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]

def solve(A):
    M = [[10**10] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            M[h][w] = A[h][w] - C*(h+w)
            if h > 0: M[h][w] = min(M[h-1][w], M[h][w])
            if w > 0: M[h][w] = min(M[h][w-1], M[h][w])
    res = 10 ** 10
    for h in range(H):
        for w in range(W):
            if h > 0: res = min(res, A[h][w] + C*(h+w) + M[h-1][w])
            if w > 0: res = min(res, A[h][w] + C*(h+w) + M[h][w-1])
    return res

ans = solve(X)
for h in range(H):
    for w in range(W//2):
        X[h][w], X[h][-w-1] = X[h][-w-1], X[h][w]

ans = min(ans, solve(X))
print(ans)