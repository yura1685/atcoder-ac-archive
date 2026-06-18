N = int(input())
A, B, C, D = [], [], [], []
for _ in range(N):
    X, Y = map(int,input().split())
    U, V = X+Y, X-Y
    if U % 2 == 0:
        A.append(U//2)
        B.append(V//2)
    else:
        C.append(U//2)
        D.append(V//2)

def f(X):
    n = len(X)
    res = 0
    X.sort()
    for i in range(n):
        res += i*X[i] - (n-i-1)*X[i]
    return res

print(f(A)+f(B)+f(C)+f(D))