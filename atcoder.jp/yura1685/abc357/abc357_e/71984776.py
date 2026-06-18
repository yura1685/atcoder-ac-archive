from atcoder.scc import SCCGraph

N = int(input())
G = SCCGraph(N)
A = list(map(int,input().split()))
for i, a in enumerate(A):
    G.add_edge(i, a-1)

ans = [0] * N
for g in G.scc()[::-1]:
    if len(g) > 1 or A[g[0]] - 1 == g[0]:
        for u in g:
            ans[u] = len(g)
    else:
        ans[g[0]] = ans[A[g[0]]-1] + 1

print(sum(ans))