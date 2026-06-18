from atcoder.scc import SCCGraph

N = int(input())
X = [0] + list(map(int,input().split()))
C = [0] + list(map(int,input().split()))

g = SCCGraph(N+1)
for i in range(N+1):
    g.add_edge(i,X[i])

ans = 0
for c in g.scc():
    if len(c) == 1:
        continue
    human = 10**9
    for u in c:
        human = min(human, C[u])
    ans += human

print(ans)