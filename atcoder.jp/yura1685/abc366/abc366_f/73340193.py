N, K = map(int,input().split())
A, B = [], []
for _ in range(N):
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)

I = list(range(N))
I.sort(key=lambda x: (A[x] - 1) / B[x])

dp = [int(-1e9)] * (K+1)
dp[0] = 1

for i in I:
    ndp = dp.copy()
    for j in range(K):
        if dp[j] > int(-1e9):
            ndp[j+1] = max(ndp[j+1], dp[j] * A[i] + B[i])
    dp = ndp

print(dp[K])