N, x, y = map(int,input().split())
a1, *A = map(int,input().split())
x -= a1

yoko, tate = [], []
for i in range(N-1):
    if i % 2 == 0:
        tate.append(A[i])
    else:
        yoko.append(A[i])

def f(X, target):
    if abs(sum(X)) < target:
        return False
    n = len(X)
    # dp[i][j]: iまでで和をjに出来るか
    dp = [[False]*(20*n+1) for _ in range(n+1)]
    dp[0][10*n] = True
    for i in range(n):
        for j in range(20*n+1):
            if dp[i][j]:
                dp[i+1][j-X[i]] = True
                dp[i+1][j+X[i]] = True
    return dp[n][10*n+target]

if f(yoko, x) and f(tate, y):
    print('Yes')
else:
    print('No')