# 計NW個の頂点
# i番目の街のj日目を W*i + j で書く

from atcoder.scc import SCCGraph

def solve():
    N, M = map(int, input().split())
    uv = []
    for _ in range(M):
        U, V = map(int, input().split())
        uv.append((U-1, V-1))
    W = int(input())

    def f(i, j):
        return W * i + j
    
    g = SCCGraph(N*W)
    S = [input() for _ in range(N)]

    for u in range(N):
        for j in range(W):
            j2 = j + 1 if j + 1 < W else 0
            if S[u][j] == 'o' and S[u][j2] == 'o':
                g.add_edge(f(u,j), f(u,j2))

    for u, v in uv:
        for j in range(W):
            j2 = j + 1 if j + 1 < W else 0
            if S[u][j] == 'o' and S[v][j2] == 'o':
                g.add_edge(f(u,j), f(v,j2))
            if S[v][j] == 'o' and S[u][j2] == 'o':
                g.add_edge(f(v,j), f(u,j2))
    
    ans = g.scc()
    for a in ans:
        if len(a) > 1:
            print('Yes')
            return 
    print('No')

T = int(input())
for _ in range(T):
    solve()