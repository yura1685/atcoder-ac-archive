from atcoder.maxflow import MFGraph
import sys
input = sys.stdin.readline

N, T = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(N)]
B = [tuple(map(int, input().split())) for _ in range(N)]
A = [(A[i][0], A[i][1], i) for i in range(N)]
A.sort()
B.sort()
B_dict = {B[i]: i+1 for i in range(N)}
D = {(T, 0): 1, (T, T): 2, (0, T): 3, (-T, T): 4, (-T, 0): 5, (-T, -T): 6, (0, -T): 7, (T, -T): 8}
G = MFGraph(2*N+2)

for i in range(1, N+1):
    G.add_edge(0, i, 1)
    G.add_edge(i + N, 2*N + 1, 1)
    ax, ay, _ = A[i-1]
    for dx, dy in D:
        bx, by = ax + dx, ay + dy
        if (bx, by) in B_dict:
            j = B_dict[(bx, by)]
            G.add_edge(i, j + N, 1)

flow = G.flow(0, 2*N + 1)
if flow < N:
    print('No')
else:
    print('Yes')
    ans = [0] * N
    for E in G.edges():
        src, dst, flow = E.src, E.dst, E.flow
        if 1 <= src <= N and flow == 1:
            ax, ay, idx = A[src-1]
            bx, by = B[dst-N-1]
            dx, dy = bx - ax, by - ay
            ans[idx] = D[(dx, dy)]
    print(*ans)