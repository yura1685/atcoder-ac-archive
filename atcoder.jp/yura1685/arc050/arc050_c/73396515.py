from math import gcd

a, b, m = map(int,input().split())
g = gcd(a,b)

def matrix(A, B, mod):
    A00 = A[0][0]*B[0][0] + A[0][1]*B[1][0]
    A01 = A[0][0]*B[0][1] + A[0][1]*B[1][1]
    A10 = A[1][0]*B[0][0] + A[1][1]*B[1][0]
    A11 = A[1][0]*B[0][1] + A[1][1]*B[1][1]
    return [[A00%mod, A01%mod], [A10%mod, A11%mod]]

def pow_matrix(A,n,mod):
    res = [[1, 0], [0, 1]]
    while n:
        if n % 2 == 1:
            res = matrix(res, A, mod)
        A = matrix(A, A, mod)
        n //= 2
    return res

def f(n, r, mod):
    if n == 0:
        return 0
    T = pow_matrix([[r, 1], [0, 1]], n, mod)
    return T[0][1]

fa = f(a, 10, m)

fb = f(b//g, pow(10, g, m), m)

print(fa * fb % m)