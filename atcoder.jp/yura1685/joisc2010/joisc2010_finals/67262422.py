from atcoder.dsu import DSU

N, M, K = map(int,input().split())
edge = []
for _ in range(M):
    u, v, w = map(int,input().split())
    u, v = u-1, v-1
    edge.append((w,u,v))
edge.sort()
edge.reverse()

dsu = DSU(N)

ans = []
cnt = 0
while cnt < N-1:
    w, u, v = edge.pop()
    if dsu.same(u,v):
        continue
    dsu.merge(u,v)
    ans.append(w)
    cnt += 1
ans.sort(reverse=True)

print(sum(ans[K-1:]))