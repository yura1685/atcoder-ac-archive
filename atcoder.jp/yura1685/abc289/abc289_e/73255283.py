from collections import deque

def solve():
    N, M = map(int,input().split())
    C = list(map(int,input().split()))
    g = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int,input().split())
        g[u-1].append(v-1)
        g[v-1].append(u-1)
    if C[0] == C[-1]:
        print(-1)
        return
    inf = float('inf')
    step = [[inf]*N for _ in range(N)]
    step[0][N-1] = 0
    dq = deque([(0,N-1)])
    while dq:
        u1, u2 = dq.popleft()
        for v1 in g[u1]:
            for v2 in g[u2]:
                if C[v1] ^ C[v2] != 1:
                    continue
                if step[u1][u2] + 1 >= step[v1][v2]:
                    continue
                step[v1][v2] = step[u1][u2] + 1
                dq.append((v1,v2))
    print(step[N-1][0] if step[N-1][0] < inf else -1)

T = int(input())
for _ in range(T):
    solve()