X, Y = map(lambda x:int(x),input().split())
mod = 10**9 + 7

def f(n):
    p = 1
    for i in range(1,n+1):
        p = p*i % mod
    return p

print(f(X+Y) * pow(f(X)*f(Y),mod-2,mod) % mod)