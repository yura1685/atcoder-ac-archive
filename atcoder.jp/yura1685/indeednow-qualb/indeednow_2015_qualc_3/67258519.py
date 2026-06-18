import heapq

N = int(input())
g = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

check = [0]*(N+1)
check[1] = 1
P = [1]
heapq.heapify(P)
ans = []

while P:
    u = heapq.heappop(P)
    ans.append(u)
    for v in g[u]:
        if check[v] == 0:
            check[v] = 1
            heapq.heappush(P,v)

print(*ans)