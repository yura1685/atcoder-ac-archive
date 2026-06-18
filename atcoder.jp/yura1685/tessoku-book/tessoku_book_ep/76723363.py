from atcoder.maxflow import MFGraph

N, M = map(int, input().split())
g = MFGraph(26 + N)
for i in range(1, N+1):
    C = input()
    g.add_edge(0, i, 10)
    for j in range(24):
        if C[j] == '0':
            continue
        g.add_edge(i, N + j + 1, 1)
for i in range(N+1, N+25):
    g.add_edge(i, N+25, M)

ans = g.flow(0, N+25)
print('Yes' if ans == 24 * M else 'No')