from atcoder.maxflow import MFGraph

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
Q = [tuple(map(int, input().split())) for _ in range(N)]
D = [[-1] * N for _ in range(N)]
Ds = set()
for i, (px, py) in enumerate(P):
    for j, (qx, qy) in enumerate(Q):
        d = (px - qx) ** 2 + (py - qy) ** 2
        D[i][j] = d
        Ds.add(d)

Ds = sorted(Ds)
ng, ok = -1, len(Ds) - 1
while ok - ng > 1:
    mid_idx = (ng + ok) // 2
    mid = Ds[mid_idx]
    G = MFGraph(2*N+2)
    for i in range(1, N+1):
        G.add_edge(0, i, 1)
        G.add_edge(i + N, 2 * N + 1, 1)
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            if D[i-1][j-1] <= mid:
                G.add_edge(i, j + N, 1)
    
    flow = G.flow(0, 2*N+1)
    if flow == N:
        ok = mid_idx
    else:
        ng = mid_idx

print(Ds[ok] ** (1/2))