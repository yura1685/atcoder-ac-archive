from atcoder.maxflow import MFGraph
import sys
read = sys.stdin.buffer.read
data = list(map(int, read().split()))

N, M, P, G = data[:4]
inf = 10 ** 9
g = MFGraph(M + 1)
L = data[4:4+G]
for n in L:
    g.add_edge(M, n, inf)
edges = data[4+G:]
for i in range(0, len(edges), 3):
    frm, to, cap = edges[i:i+3]
    g.add_edge(frm, to, cap)
flow = g.flow(M, 0)
print('Yes' if flow >= P else 'No')