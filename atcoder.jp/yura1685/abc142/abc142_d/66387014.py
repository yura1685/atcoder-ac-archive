from math import gcd

A, B = map(int,input().split())

g = gcd(A,B)

def prime_factorize(n):
    a = [1]
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

x = prime_factorize(g)
print(len(set(x)))