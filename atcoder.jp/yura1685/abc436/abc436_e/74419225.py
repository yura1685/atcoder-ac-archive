from atcoder.dsu import DSU

N = int(input())
uf = DSU(N)
P = [int(x) - 1 for x in input().split()]
for i in range(N): uf.merge(i, P[i])

ans = 0
for g in uf.groups():
    n = len(g)
    ans += n * (n-1) // 2

print(ans)