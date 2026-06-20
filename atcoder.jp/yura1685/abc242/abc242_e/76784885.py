def solve():
    N = int(input())
    M = (N + 1) // 2
    S = input()
    dp = [0] * (M + 1)
    for i, s in enumerate(S[:M]):
        dp[i+1] = (dp[i] * 26 + ord(s) - 65) % mod
    S2 = S[:M-(N%2)] + S[M-1::-1]
    print((dp[-1] + (S2 <= S)) % mod)
    
mod = 998244353
T = int(input())
for _ in range(T):
    solve()