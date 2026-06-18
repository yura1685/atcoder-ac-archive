def fib(n,l):
    c = [1]*(l)
    for _ in range(n-1):
        x = c[-1] + c[-l]
        x %= (10**9+7)
        c.append(x)
    return c[-1]

N, L = map(int,input().split())
print(fib(N-L+2,L))