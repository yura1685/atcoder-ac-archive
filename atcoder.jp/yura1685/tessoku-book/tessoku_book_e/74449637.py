def f(n):
    return 0 if n < 3 else (n-2) * (n-1) // 2

N, K = map(int, input().split())
ans = f(K) - 3 * f(K-N) + 3 * f(K-2*N) - f(K-3*N)
print(ans)