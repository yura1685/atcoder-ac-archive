import heapq

N, M = map(int,input().split())
g = [[] for _ in range(N)] # 有向グラフ
c = [0]*N # 頂点iが終点となっているパスの個数

for _ in range(M):
    x, y = map(int,input().split())
    x, y = x-1, y-1
    g[x].append(y)
    c[y] += 1

d = []
heapq.heapify(d)
ans = []

for i in range(N): # まず、最初のところ
    if c[i] == 0:
        heapq.heappush(d,i)

num = 1
while d:
    u = heapq.heappop(d)
    ans.append(u+1)
    num += 1
    for v in g[u]:
        c[v] -= 1
        if c[v] == 0:
            heapq.heappush(d,v)

if len(ans) < N:
    print(-1)
else:
    print(*ans)