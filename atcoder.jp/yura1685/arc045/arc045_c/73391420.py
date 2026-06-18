from collections import deque, defaultdict

N, X = map(int,input().split())
g = [[] for _ in range(N)]
for _ in range(N-1):
    x, y, c = map(int,input().split())
    g[x-1].append((y-1,c))
    g[y-1].append((x-1,c))

dq = deque([(0,0)]) # 頂点，xor
visit = [True] + [False] * (N-1)
d = defaultdict(int)
d[0] = 1
ans = 0

while dq:
    u, xor = dq.popleft()
    for v, w in g[u]:
        if visit[v]:
            continue
        visit[v] = True
        cur = xor ^ w
        dq.append((v, cur))
        d[cur] += 1
        ans += d[cur^X]

if X:
    print(ans)

else:
    ans = 0
    for n in d.values():
        ans += n*(n-1)//2
    print(ans)