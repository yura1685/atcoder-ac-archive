N, C = map(int, input().split())
S = []
T = []
for _ in range(N):
    x, v = map(int, input().split())
    S.append((x, v))
    T.append((C-x, v))
T.reverse()

def f(X):
    cal = 0
    res = 0
    for x, v in X:
        cal += v
        res = max(res, cal - x)
    return res

def g(X, Y):
    res = 0
    cal = 0
    Z = [0]
    for x, v in X:
        cal += v
        Z.append(cal - x)
    for i in range(1, N+1):
        Z[i] = max(Z[i], Z[i-1])
    cal = 0
    for i, (y, v) in enumerate(Y):
        cal += v
        res = max(res, cal + Z[N-i-1] - 2 * y)
    return res

ans = max(f(S), f(T), g(S, T), g(T, S))
print(ans)