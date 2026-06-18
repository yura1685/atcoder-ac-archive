X, A, D, N = map(int,input().split())

X -= A
if D <= 0:
    D = -D
    X = -X
if X <= 0:
    print(-X)
    exit()
if X >= D*(N-1):
    print(X-D*(N-1))
    exit()

t = X % D
print(min(t,D-t))