N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
S = [[] for _ in range(N)]
dp = [[0]*(max(B)+1) for _ in range(N)]
mod = 998244353

def accumulate(L):
    res = [0] * len(L)
    res[0] = L[0]
    for i in range(len(L)-1):
        res[i+1] = (res[i] + L[i+1]) % mod
    return res

for i in range(A[0], B[0]+1):
    dp[0][i] = 1
S[0] = accumulate(dp[0])

for i in range(1,N):
    a, b = A[i], B[i]
    for j in range(a,b+1):
        dp[i][j] = S[i-1][j]
    S[i] = accumulate(dp[i])

print(sum(dp[-1]) % mod)