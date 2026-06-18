from collections import deque

N = int(input())

g = [[] for _ in range(N)]
time = []
for i in range(N):
    X = [int(x) for x in input().split()]
    time.append(X[0])
    for j in range(2,2+X[1]):
        g[i].append(X[j]-1)

d = deque([N-1])
c = [0]*N
c[N-1] = 1

ans = 0
while d:
    u = d.popleft()
    ans += time[u]
    for v in g[u]:
        if c[v] == 0:
            c[v] = 1
            d.append(v)

print(ans)