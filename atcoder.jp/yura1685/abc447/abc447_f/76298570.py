from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

def solve():
    N = int(input())
    g = [[] for _ in range(N)]
    dim = [0] * N
    for _ in range(N-1):
        A, B = map(int, input().split())
        g[A-1].append(B-1)
        g[B-1].append(A-1)
        dim[A-1] += 1
        dim[B-1] += 1
    dist = [[-1] * N for _ in range(2)]

    def dfs(u, p):
        if dim[u] <= 2:
            dist[0][u] = dist[1][u] = 0
            return 0
        elif dim[u] == 3:
            M = 0
            for v in g[u]:
                if v == p: continue
                M = max(M, dfs(v, u))
            dist[0][u] = M
            return 1
        else:
            M1, M2 = 0, 0
            for v in g[u]:
                if v == p: continue
                M = dfs(v, u)
                if M2 >= M: continue
                elif M1 >= M >= M2: M2 = M
                elif M >= M1: M1, M2 = M, M1
            dist[0][u] = M1
            dist[1][u] = M2
            return M1 + 1
    
    for i in range(N):
        if dist[0][i] == -1:
            dfs(i, -1)

    ans = 1
    for i in range(N):
        if dim[i] <= 2: continue
        if dim[i] == 3: ans = max(ans, dist[0][i] + 1)
        if dim[i] >= 4: ans = max(ans, dist[0][i] + dist[1][i] + 1)
    print(ans)

T = int(input())
for _ in range(T):
    solve()