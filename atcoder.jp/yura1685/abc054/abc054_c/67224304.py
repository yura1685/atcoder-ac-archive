from itertools import permutations

N, M = map(int,input().split())
g = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

ans = 0
for p in permutations([i for i in range(2,N+1)]):
    p = [1] + list(p)
    if all([p[i+1] in g[p[i]] for i in range(N-1)]):
        ans += 1
        
print(ans)