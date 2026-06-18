import heapq

N, M, T = map(int,input().split())
A = list(map(int,input().split()))

g1 = [[] for _ in range(N)]
g2 = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int,input().split())
    g1[a-1].append((b-1,c))
    g2[b-1].append((a-1,c))

def f(g):
    dis = [float('inf')]*N
    dis[0] = 0
    P = [(0,0)]
    heapq.heapify(P)
    while P:
        w, u = heapq.heappop(P)
        d = {}
        for v, q in g[u]:
            if dis[v] > w+q:
                dis[v] = w+q
                d[v] = w+q
        for s in d:
            heapq.heappush(P,(d[s],s))
    return dis

d1 = f(g1)
d2 = f(g2)

ans = 0
for i in range(N):
    ans = max(ans,max(0,(T-d1[i]-d2[i])*A[i]))
print(ans)