from atcoder.dsu import DSU

N, M = map(int, input().split())
dim = [0] * N
uf = DSU(N)
for _ in range(M):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    dim[u] += 1
    dim[v] += 1
    uf.merge(u, v)

mod = 998244353
ans = 1

for group in uf.groups():
    cnt = 0
    for u in group:
        cnt += dim[u]
    if cnt != 2 * len(group):
        ans = 0
    else:
        ans = ans * 2 % mod

print(ans)