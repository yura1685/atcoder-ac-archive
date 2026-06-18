from collections import deque

I = input().split()
M, A, B = int(I[0]), int(I[1]), int(I[2])

g = [-1] * M*M
for s1 in range(M):
    for s2 in range(M):
        x, y = s1, s2
        while g[M*x + y] == -1:
            z = (A*y + B*x) % M
            g[M*x + y] = M*y + z
            x, y = y, z

rev_g = [[] for _ in range(M*M)]
for i in range(M*M):
    rev_g[g[i]].append(i)

ans = [True] * M*M

for s in range(M):
    dq = deque()
    if ans[s*M]: dq.append(s*M)
    if ans[s]:   dq.append(s)
    ans[s*M] = ans[s] = False
    while dq:
        u = dq.popleft()
        for v in rev_g[u]:
            if not ans[v]:
                continue
            ans[v] = False
            dq.append(v)

print(sum(ans))