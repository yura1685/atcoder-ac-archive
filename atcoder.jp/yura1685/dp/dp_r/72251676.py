mod = 10**9 + 7
N, K = map(int,input().split())
X = [list(map(int,input().split())) for _ in range(N)]
I = [[1 if i == j else 0 for j in range(N)] for i in range(N)]

def f(A,B):
    X = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                X[i][j] += A[i][k] * B[k][j]
            X[i][j] %= mod
    return X

def pow(A,n,B):
    res = B
    base = A
    while n:
        if n % 2 == 1:
            res = f(res, base)
        base = f(base, base)
        n //= 2
    return res

P = pow(X, K, I)

ans = 0
print(sum(sum(p) for p in P) % mod)