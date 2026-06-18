def f(n):
    if n == 0:
        return 1
    else:
        return n*f(n-1)

def g(n,r):
    return f(n)//(f(n-r)*f(r))

n = int(input())
for i in range(n):
    U = []
    for j in range(i+1):
        U.append(g(i,j))
    print(*U)