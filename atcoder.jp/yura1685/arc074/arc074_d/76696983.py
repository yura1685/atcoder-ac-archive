from atcoder.maxflow import MFGraph

inf = 10 ** 18
H, W = map(int, input().split())
N = (H + 1) * (W + 1)

G = MFGraph(3 * N)
A = [input() for _ in range(H)]

for h in range(1, H+1):
    for w in range(1, W+1):
        row_node = 2 * N + h
        col_node = 2 * N + H + w

        if A[h-1][w-1] == '.':
            continue
        if A[h-1][w-1] == 'S':
            s_up = h * (W + 1) + w
            s_do = s_up + N
            G.add_edge(s_up, s_do, inf)
            G.add_edge(s_do, row_node, inf)
            G.add_edge(row_node, s_up, inf)
            G.add_edge(s_do, col_node, inf)
            G.add_edge(col_node, s_up, inf)
        elif A[h-1][w-1] == 'T':
            t_up = h * (W + 1) + w
            t_do = t_up + N
            G.add_edge(t_up, t_do, inf)
            G.add_edge(t_do, row_node, inf)
            G.add_edge(row_node, t_up, inf)
            G.add_edge(t_do, col_node, inf) 
            G.add_edge(col_node, t_up, inf)
        else:
            up = h * (W + 1) + w
            do = up + N
            G.add_edge(up, do, 1)
            G.add_edge(do, row_node, inf)
            G.add_edge(row_node, up, inf)
            G.add_edge(do, col_node, inf)
            G.add_edge(col_node, up, inf)

flow = G.flow(s_up, t_do)
print(flow if flow < inf else -1)