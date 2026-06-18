def f(n):
    u = list(str(n))
    g2, g1 = sorted(u), sorted(u,reverse=True)
    c, d = int(''.join(g1)), int(''.join(g2))
    return c - d

N, K = map(int,input().split())
for i in range(K):
    N = f(N)

print(N)