from itertools import permutations

N = int(input())

Gm = [[] for _ in range(N)]
Gh = [[] for _ in range(N)]

Mg = int(input())
for _ in range(Mg):
    u, v = map(int,input().split())
    u, v = u-1, v-1
    Gm[u].append(v)
    Gm[v].append(u)

Mh = int(input())
for _ in range(Mh):
    u, v = map(int,input().split())
    u, v = u-1, v-1
    Gh[u].append(v)
    Gh[v].append(u)

A = []
for i in range(N-1):
    X = [0]*(i+1) + list(map(int,input().split()))
    A.append(X)
A += [[0]*N]
per = list(permutations([i for i in range(N)]))

ans = 10**10
for p in per: # Gの頂点uを、p[u]を介して扱う
    q = 0
    for u in range(N):
        x = []
        for v in range(N):
            if (v in Gh[u] and p[v] not in Gm[p[u]]) or (v not in Gh[u] and p[v] in Gm[p[u]]):
                if u != v:
                    x.append(v)
        for v in x:
            q += A[u][v]
    ans = min(ans,q)

print(ans)