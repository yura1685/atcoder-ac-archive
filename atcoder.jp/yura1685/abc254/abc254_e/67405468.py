from collections import deque, defaultdict


N, M = map(int,input().split())
g = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

Q = int(input())
for _ in range(Q):
    x, k = map(int,input().split())
    q = deque([(0,x)])
    d = defaultdict(int)
    d[x] = 1
    ans = 0
    while q:
        w, u = q.popleft()
        ans += u
        if w == k:
            continue
        for v in g[u]:
            if d[v] == 0:
                d[v] = 1
                q.append((w+1,v))
    print(ans)