def f(a, b):
    m, M = min(a, b), max(a, b)
    if m == M:
        return m
    if m == 0:
        return -M
    k = M // m
    return 2 * m * k + f(m, M - k*m)

N, X = map(int,input().split())
print(N+f(X,N-X))