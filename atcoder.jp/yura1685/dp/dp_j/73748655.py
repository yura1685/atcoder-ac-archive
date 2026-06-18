N = int(input())
A = list(map(int,input().split()))
c1 = A.count(1)
c2 = A.count(2)
c3 = A.count(3)

dp = [[[0.0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]

for k in range(N+1):
    for j in range(N-k+1):
        for i in range(N-k-j+1):
            if i == j == k == 0:
                continue
            res = float(N)
            if i > 0:
                res += i * dp[k][j][i-1]
            if j > 0:
                res += j * dp[k][j-1][i+1]
            if k > 0:
                res += k * dp[k-1][j+1][i]
            
            dp[k][j][i] = res / (i + j + k)
    
print(dp[c3][c2][c1])