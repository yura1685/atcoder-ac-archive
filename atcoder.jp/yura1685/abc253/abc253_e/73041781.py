mod = 998244353
N, M, K = map(int,input().split())
dp = [[0] * (M+1) for _ in range(N)]
dp[0] = [0] + [1] * M

if K == 0: exit(print(pow(M,N,mod)))

def accumulate(L):
    res = [L[0]]
    for i in range(1,len(L)):
        res.append((L[i] + res[-1]) % mod)
    return res

S = [accumulate(dp[0])]

for i in range(1,N):
    for j in range(1,M+1):
        if j - K > 0:
            dp[i][j] += S[i-1][j-K]
        if j + K <= M:
            dp[i][j] += S[i-1][M] - S[i-1][j+K-1]
    S.append(accumulate(dp[i]))

print(sum(dp[-1]) % mod)