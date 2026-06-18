N = int(input())
dp = [i for i in range(N+1)]

for n in range(1,N+1):
    t6, t9 = 1, 1
    while n - 6 ** t6 >= 0:
        dp[n] = min(dp[n], dp[n-6**t6] + 1)
        t6 += 1
    while n - 9 ** t9 >= 0:
        dp[n] = min(dp[n], dp[n-9**t9] + 1)
        t9 += 1

print(dp[-1])