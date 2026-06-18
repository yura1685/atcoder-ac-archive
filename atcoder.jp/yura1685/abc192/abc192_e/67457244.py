import heapq

N, M, X, Y = map(int,input().split())

train = [[] for _ in range(N+1)] # 目的地，時間，発車時刻
for _ in range(M):
    A, B, T, K = map(int,input().split())
    train[A].append((B,T,K))
    train[B].append((A,T,K))

dis = [float('inf')]*(N+1)
dis[X] = 0

Q = [(0, X)] # 時間，駅
heapq.heapify(Q)
check = [0]*(N+1)

while Q:
    s, u = heapq.heappop(Q) # 時刻 s に駅 u にいるで
    if check[u] == 0:
        check[u] = 1
    else:
        continue
    for v, t, k in train[u]: # 駅 v まで t，次の発車時刻は k の倍数
        pue = (s+k-1)//k * k # 次の発車時刻
        if pue + t < dis[v]:
            dis[v] = pue + t
            heapq.heappush(Q,(pue+t,v))

print(dis[Y] if dis[Y] < float('inf') else -1)