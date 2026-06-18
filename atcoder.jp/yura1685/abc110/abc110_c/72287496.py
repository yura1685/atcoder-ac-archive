S, T = input(), input()
N = len(S)

def f(X, Y):
    d = dict()
    for i in range(N):
        if d.get(X[i]) and d[X[i]] != Y[i]:
            return False
        if not d.get(X[i]):
            d[X[i]] = Y[i]
    return True

print('Yes' if f(S, T) and f(T, S) else 'No')