from atcoder.dsu import DSU

N, M = map(int, input().split())
A = list(map(int, input().split()))
uf = DSU(N)
E = []
for i in range(N):
    for j in range(i+1, N):
        x, y = A[i], A[j]
        c = (pow(x, y, M) + pow(y, x, M)) % M
        E.append((c, i, j))
E.sort(reverse=True)
ans = 0
for c, i, j in E:
    if uf.same(i, j):
        continue
    ans += c
    uf.merge(i, j)

print(ans)