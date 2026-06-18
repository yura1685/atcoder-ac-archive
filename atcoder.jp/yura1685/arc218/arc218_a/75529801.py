from collections import Counter

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
C = [[] for _ in range(N*M)]
for n in range(N):
    for m in range(M):
        C[A[n][m]-1].append(n)

mod = 998244353
ans = 0
for x in range(N*M):
    Cnt = Counter(C[x])
    t = 1
    for n in Cnt.values():
        t *= M - n
        t %= mod
    t = t * pow(M, N - len(Cnt), mod) % mod
    ans += t

print((pow(M, N, mod) * M * N - ans) % mod)