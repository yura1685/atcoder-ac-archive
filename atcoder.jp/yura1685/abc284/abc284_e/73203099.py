N, M = map(int,input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int,input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

limit = 10**6
ans = 0
check = [0] * N

stack = [(0,0)]

while stack and ans < limit:
    u, p = stack.pop()
    if p == 0:
        if check[u]:
            continue
        check[u] = 1
        ans += 1
        if ans == limit:
            break
        stack.append((u,1))
        for v in g[u]:
            if not check[v]:
                stack.append((v,0))
    else:
        check[u] = 0

print(ans)