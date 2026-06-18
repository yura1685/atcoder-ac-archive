from collections import deque

N = int(input())
S = [input() for _ in range(N)]
g = [[] for _ in range(N)]

for u in range(N):
    for v in range(N):
        if S[u][v] == '1':
            g[v].append(u)

ans = 0
for u in range(N):
    cnt = 1
    dq = deque([u])
    check = [False] * N
    check[u] = True
    while dq:
        v = dq.popleft()
        for w in g[v]:
            if check[w] == False:
                check[w] = True
                dq.append(w)
                cnt += 1
    ans += 1 / cnt

print(ans)