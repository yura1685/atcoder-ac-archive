H, W, K = map(int, input().split())
mod = 10 ** 9 + 7
dp = [1] + [0] * (W-1)
fib = [1, 1, 2, 3, 5, 8, 13, 21, 34]
for _ in range(H):
    dp2 = [0] * W
    for i in range(W):
        dp2[i] += dp[i] * fib[W-i-1] * fib[i]
        if i > 0:
            dp2[i] += dp[i-1] * fib[W-i-1] * fib[i-1]
        if i + 1 < W:
            dp2[i] += dp[i+1] * fib[W-i-2] * fib[i]
        dp2[i] %= mod
    dp = dp2

print(dp[K-1])