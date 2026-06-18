def f(a, b):
    return -(-a//b)

A, M, L, R = map(int, input().split())

l = f(L-A, M)
r = (R-A)//M

print(max(0, r-l+1))