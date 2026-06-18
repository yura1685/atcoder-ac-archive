from collections import deque
first, last = input().split()
N = int(input())
L = len(first)
inf = 10**8
S = [first] + [input() for _ in range(N)] + [last]
if first == last: exit(print(0, first, last, sep='\n'))
g = [[] for _ in range(N+2)]
for u in range(N+1):
    for v in range(u+1, N+2):
        s, t = S[u], S[v]
        d = 0
        for i in range(L):
            if s[i] != t[i]:
                d += 1
        if d == 1:
            g[u].append(v)
            g[v].append(u)

From = [-1] * (N+2)
Dist = [0] + [inf] * (N+1)
dq = deque([0])
while dq:
    u = dq.popleft()
    for v in g[u]:
        if Dist[v] == inf:
            Dist[v] = Dist[u] + 1
            dq.append(v)
            From[v] = u

if Dist[N+1] == inf: exit(print(-1))

path = [N+1]

while True:
    u = path[-1]
    v = From[u]
    if v == -1:
        break
    path.append(v)

path.reverse()
print(len(path) - 2)
for i in path:
    print(S[i])