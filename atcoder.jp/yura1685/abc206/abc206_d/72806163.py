from atcoder.dsu import DSU

N = int(input())
A = list(map(int,input().split()))

uf = DSU(200001)

for i in range(N//2):
    u, v = A[i], A[N-1-i]
    if u == v:
        continue
    uf.merge(u,v)

ans = 0
for g in uf.groups():
    ans += len(g) - 1

print(ans)