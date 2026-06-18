from collections import deque
from atcoder.dsu import DSU

N, M = map(int, input().split())
g = [[] for _ in range(N)]
uf = DSU(N)
for _ in range(M):
    X, Y, Z = map(int, input().split())
    g[X-1].append((Y-1, Z))
    g[Y-1].append((X-1, Z))
    uf.merge(X-1, Y-1)

check = [-1] * N
for lst in uf.groups():
    i = lst[0]
    dq = deque([i])
    check[i] = 0
    while dq:
        u = dq.popleft()
        for v, w in g[u]:
            if check[v] == -1:
                check[v] = check[u] ^ w
                dq.append(v)
            else:
                if check[v] != check[u] ^ w:
                    exit(print(-1))

visit = [False] * N
ans = [-1] * N
for lst in uf.groups():
    l = lst[0]
    visit[l] = True
    cnt1 = [0] * 30
    dq = deque([(l, 0)])
    while dq:
        u, xor = dq.popleft()
        for v, w in g[u]:
            if visit[v]:
                continue
            visit[v] = True
            nxt = xor ^ w
            dq.append((v, nxt))
            for bit in range(30):
                if (nxt >> bit) & 1:
                    cnt1[bit] += 1
    n = 0
    for i in range(30):
        if cnt1[i] > uf.size(l) - cnt1[i]:
            n |= 1 << i
    ans[l] = n
    dq2 = deque([l])
    while dq2:
        u = dq2.popleft()
        for v, w in g[u]:
            if ans[v] >= 0:
                continue
            ans[v] = ans[u] ^ w
            dq2.append(v)

print(*ans)