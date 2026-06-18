N = int(input())
ng = [int(input()) for _ in range(3)]
if N in ng:
    print('NO')
    exit()

dp = [1685]*301
dp[N] = 0
check = [N]
while check:
    if 0 in check:
        break
    n = check.pop(check.index(max(check)))
    a, b, c = n-1, n-2, n-3
    if a not in ng and a >= 0:
        dp[a] = min(dp[a],dp[n]+1)
        if a not in check:
            check.append(a)
    if b not in ng and b >= 0:
        dp[b] = min(dp[b],dp[n]+1)
        if b not in check:
            check.append(b)
    if c not in ng and c >= 0:
        dp[c] = min(dp[c],dp[n]+1)
        if c not in check:
            check.append(c)

print('YES' if dp[0] <= 100 else 'NO')