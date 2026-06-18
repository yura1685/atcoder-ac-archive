from collections import deque, defaultdict

N = int(input())

ver = [0]*N
edge = []
g = defaultdict(list)

for _ in range(N-1):
    a, b = map(int,input().split())
    a, b = a-1, b-1
    ver[a] += 1
    ver[b] += 1
    edge.append((a,b))
    g[a].append(b)
    g[b].append(a)

color = max(ver)
d = {}
dq = deque()

u = 0

cnt = 1
for v in g[0]:
    d[(0,v)] = cnt
    d[(v,0)] = cnt
    cnt += 1
    dq.append((0,v))

while dq:
    u, v = dq.popleft()
    used = d[(u,v)]
    cnt = 1 + (used == 1)
    for w in g[v]:
        if w == u:
            continue
        d[(v,w)] = cnt
        d[(w,v)] = cnt
        dq.append((v,w))
        cnt += 1
        if cnt == used:
            cnt += 1

print(color)
for u, v in edge:
    print(d[(u,v)])