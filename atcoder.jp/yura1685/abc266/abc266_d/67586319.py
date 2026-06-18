from collections import defaultdict
N = int(input())

L = [(-1,-1)]*100001
T = 0
for _ in range(N):
    t, x, a = map(int,input().split())
    T = t
    L[t] = (x,a)

dp = [[-float('inf')]*7 for _ in range(T+1)]
dp[0][1] = 0

for i in range(1,T+1):
    for j in range(1,6):
        dp[i][j] = max(dp[i-1][j-1:j+2]) + L[i][1]*(L[i][0] == j-1)

print(max(dp[-1]))