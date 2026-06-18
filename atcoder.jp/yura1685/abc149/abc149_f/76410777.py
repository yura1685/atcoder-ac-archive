from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

N = int(input())
g = [[] for _ in range(N)]
for _ in range(N-1):
    A, B = map(int, input().split())
    g[A-1].append(B-1)
    g[B-1].append(A-1)

C = [[] for _ in range(N)]
def dfs(u, f):
    res = 1
    for v in g[u]:
        if v == f:
            continue
        n = dfs(v, u)
        C[u].append(n)
        res += n
    return res

dfs(0, -1)
for i in range(1, N):
    C[i].append(N - 1 - sum(C[i]))

mod = 10 ** 9 + 7

pow2 = [1] * (N+1)
for i in range(1, N+1):
    pow2[i] = pow2[i-1] * 2 % mod
inv2 = [1] * (N+1)
inv2[N] = pow(pow2[N], -1, mod)
for i in range(N-1, -1, -1):
    inv2[i] = inv2[i+1] * 2 % mod

ans = 0
for L in C:
    if len(L) == 1:
        continue
    x = 1
    for n in L:
        x -= inv2[N-n-1]
        x %= mod
    x += (len(L) - 1) * inv2[N-1]
    x = x * inv2[1] % mod
    ans += x

print(ans % mod)