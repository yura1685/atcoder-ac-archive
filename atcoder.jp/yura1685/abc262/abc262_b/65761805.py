N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

score = 0

for a in range(1,N-1):
    for b in range(a+1,N):
        for c in range(b+1,N+1):
            if b in graph[a] and c in graph[b] and a in graph[c]:
                score += 1

print(score)