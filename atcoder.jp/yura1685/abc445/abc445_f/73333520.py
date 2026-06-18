N, K = map(int,input().split())
X = [list(map(int,input().split())) for _ in range(N)]
inf = float('inf')

def matrix(A,B):
    C = [[inf]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] = min(C[i][j], A[i][k] + B[k][j])
    return C

ans = X
K -= 1
while K:
    if K % 2:
        ans = matrix(ans, X)
    X = matrix(X, X)
    K //= 2

for i in range(N):
    print(ans[i][i])