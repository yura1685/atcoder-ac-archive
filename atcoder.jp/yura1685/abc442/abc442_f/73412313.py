from itertools import accumulate

N = int(input())
S = [input()[::-1] for _ in range(N)]

def left_accumulate(L):
    res = [0] * (N+1)
    for i in range(N):
        if L[i] == '.':
            res[i+1] = 1
    return list(accumulate(res))

def right_accumulate(L):
    res = [0] * (N+1)
    for i in range(N):
        if L[-i-1] == '#':
            res[i+1] = 1
    return list(accumulate(res))[::-1]

ac = [[left_accumulate(s), right_accumulate(s)] for s in S]

inf = N**2 + 1685
dp = [[inf]*(N+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(1,N+1):
    dp[0][i] = 0
    dp[i][0] = dp[i-1][0] + ac[i-1][1][0]

for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j] = min(dp[i][j-1],
                       dp[i-1][j] + ac[i-1][0][j] + ac[i-1][1][j])

print(dp[-1][-1])