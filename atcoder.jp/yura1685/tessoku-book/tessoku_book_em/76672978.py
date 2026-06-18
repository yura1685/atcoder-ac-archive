from atcoder.dsu import DSU

N, M = map(int, input().split())
Edges = [tuple(map(int, input().split())) for _ in range(M)]
Flags = [True] * M

Q = int(input())
query = []
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x = q[1]
        Flags[x-1] = False
        query.append((1, x, 0))
    else:
        u, v = q[1:]
        query.append((2, u, v))

uf = DSU(N)
for i in range(M):
    if Flags[i]:
        a, b = Edges[i]
        uf.merge(a-1, b-1)

query.reverse()
ans = []
for q, a, b in query:
    if q == 1:
        u, v = Edges[a-1]
        uf.merge(u-1, v-1)
    else:
        ans.append(uf.same(a-1, b-1))
ans.reverse()

for a in ans:
    print('Yes' if a else 'No')