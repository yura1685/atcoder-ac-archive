from sortedcontainers import SortedSet

N, M, K = map(int,input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

s = SortedSet()
for _ in range(K):
    p, h = map(int,input().split())
    s.add((h,p-1))

X = [-1] * N
for h, p in s:
    X[p] = h

Conf = [0] * N
while s:
    h, p = s.pop()
    Conf[p] = 1
    if h == 1:
        for v in g[p]:
            Conf[v] = 1
    else:
        for v in g[p]:
            if Conf[v]: continue
            if X[v] >= h-1: continue
            if X[v] == -1:
                X[v] = h-1
                s.add((h-1,v))
            else:
                s.discard((X[v],v))
                s.add((h-1,v))

ans = [i+1 for i in range(N) if Conf[i]]
print(len(ans))
print(*ans)