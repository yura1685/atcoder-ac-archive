from sympy import factorint

N, P = map(int,input().split())

p = factorint(P)

ans = 1
for v in p:
    ans *= v**(p[v]//N)

print(ans)