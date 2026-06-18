from sympy import primerange

def legendre(n,p):
    p2 = p
    ans = 0
    while True:
        c = n//p2
        if c == 0:
            return ans
        ans += c
        p2 *= p

N = int(input())

P = list(primerange(1, N+1))

hoge = 1
for p in P:
    hoge = hoge*(legendre(N,p)+1)%(10**9+7)

print(hoge)