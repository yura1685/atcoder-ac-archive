from atcoder.scc import SCCGraph

N = int(input())
A = [int(x)-1 for x in input().split()]
G = SCCGraph(N)
for i, a in enumerate(A):
    G.add_edge(i, a)

scc = G.scc()
ans = 0
for g in scc:
    if len(g) > 1 or A[g[0]] == g[0]:
        ans += len(g)

print(ans)