N, M, P = map(int,input().split())
g = [] # 始点，終点，スコア

for _ in range(M):
    a, b, c = map(int,input().split())
    g.append((a-1,b-1,c-P))

d = [-float('inf')]*N
d[0] = 0
for i in range(N):
    update = False
    for a, b, c in g:
        if d[b] < d[a] + c:
            d[b] = d[a] + c
            update = True
            if i == N-1:
                d[b] = float('inf')

for i in range(N):
    for a, b, c in g:
        if d[b] < d[a] + c:
            d[b] = d[a] + c

print(max(0,d[N-1]) if d[N-1] < float('inf') else -1)