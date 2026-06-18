from atcoder.scc import SCCGraph

N, M = map(int,input().split())
g = SCCGraph(N)
for _ in range(M):
    a, b = map(int,input().split())
    g.add_edge(a,b)

G = g.scc()

print(len(G))

for l in G:
    ans = [len(l)] + l
    print(*ans)
