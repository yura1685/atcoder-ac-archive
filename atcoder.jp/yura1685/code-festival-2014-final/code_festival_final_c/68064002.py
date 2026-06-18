def f(X):
    Y = str(X)
    n = len(Y)
    t = 0
    for i in range(n):
        t += int(Y[-i-1])*pow(X,i)
    return t

A = int(input())
for n in range(10,10001):
    if f(n) == A:
        exit(print(n))
print(-1)