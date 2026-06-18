from atcoder.dsu import DSU

N, M = map(int,input().split())
if N != M+1:
    print('No')
    exit()

yura = [0]*N
graph = DSU(N+1)
for _ in range(M):
    u, v = map(int,input().split())
    graph.merge(u,v)
    yura[u-1] += 1
    yura[v-1] += 1

if graph.size(1) == N and yura.count(1) == 2 and yura.count(2) == N-2:
    print('Yes')
else:
    print('No')