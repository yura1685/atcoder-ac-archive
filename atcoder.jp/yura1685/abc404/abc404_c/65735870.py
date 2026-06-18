from atcoder.dsu import DSU

N, M = map(int,input().split())
dsu = DSU(N+1)

count = [0]*(N+1)

for i in range(M):
    a, b = map(int,input().split())
    count[a] += 1
    count[b] += 1
    dsu.merge(a,b)

graph1 = dsu.leader(1)
for i in range(2,N+1):
    if dsu.leader(i) != graph1:
        print('No')
        exit()

for i in range(N):
    if count[i+1] != 2:
        print('No')
        exit()
print('Yes')