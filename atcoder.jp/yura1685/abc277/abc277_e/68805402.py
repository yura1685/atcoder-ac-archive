import heapq

N, M, K = map(int,input().split())
INF = float('INF')

g = [[[], []] for _ in range(N)]

for _ in range(M):
    u, v, a = map(int,input().split())
    g[u-1][a].append(v-1)
    g[v-1][a].append(u-1)

S = [0]*N
for i in input().split(): S[int(i)-1] = 1

m = [[INF,INF] for _ in range(N)]
m[0][1] = 0

hq = []
heapq.heapify(hq)
heapq.heappush(hq,(0,0,1)) # 距離，頂点，スイッチ

while hq:
    d, u, s = heapq.heappop(hq)
    # スイッチを押さない場合
    for v in g[u][s]:
        if d + 1 < m[v][s]:
            m[v][s] = d + 1
            heapq.heappush(hq,(d+1,v,s))
    # スイッチを押す場合
    if S[u]:
        if d < m[u][1-s]:
            m[u][1-s] = d
            heapq.heappush(hq,(d,u,1-s))

print(min(m[-1]) if min(m[-1]) < INF else -1)