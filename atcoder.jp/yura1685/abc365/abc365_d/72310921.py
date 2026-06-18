N = int(input())
S = input()
dp = [[0]*N for _ in range(3)]

d = {'R':0, 'S':1, 'P':2}

dp[(d[S[0]]+2) % 3][0] = 1
dp[(d[S[0]]+1) % 3][0] = - 1685

for i in range(1,N):
    dp[(d[S[i]] + 1) % 3][i] = - 1685
    dp[(d[S[i]] + 2) % 3][i] = 1 + max(dp[d[S[i]] % 3][i-1],
                                       dp[(d[S[i]] + 1) % 3][i-1])
    dp[d[S[i]] % 3][i] = max(dp[(d[S[i]] + 1) % 3][i-1], 
                             dp[(d[S[i]] + 2) % 3][i-1])

print(max(dp[i][-1] for i in range(3)))