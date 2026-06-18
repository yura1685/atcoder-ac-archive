from atcoder.maxflow import MFGraph

inf = 10 ** 18
N, M = map(int, input().split())
G = MFGraph(2*N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    G.add_edge(a + N, b, inf)
    G.add_edge(b + N, a, inf)
C = list(map(int, input().split()))
for i in range(2, N):
    G.add_edge(i, i + N, C[i-1])

flow = G.flow(1 + N, N)
mc = G.min_cut(1 + N)
ans = [i for i in range(2, N) if mc[i] and not mc[i+N]]
print(flow)
print(len(ans))
print(*ans)