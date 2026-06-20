def solve(Y:int) -> int:
    X = str(Y)
    N = len(X)
    dp = [[0, 0] for _ in range(N+1)]
    dp[0][1] = 1
    for i, x in enumerate(X):
        n = int(x)
        for b in range(2):
            if dp[i][b] == 0:
                continue
            if b == 0:
                for m in range(10):
                    if m == 4 or m == 9:
                        continue
                    dp[i+1][0] += dp[i][0]
            else:
                for m in range(n):
                    if m == 4 or m == 9:
                        continue
                    dp[i+1][0] += dp[i][1]
                if n != 4 and n != 9:
                    dp[i+1][1] += dp[i][1]
    return Y + 1 - sum(dp[N])

A, B = map(int, input().split())
print(solve(B) - solve(A-1))