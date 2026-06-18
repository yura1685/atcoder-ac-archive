from collections import deque

N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

nibu = True
C = [-1] * N
C[0] = 0
dq = deque([0])
while dq:
    u = dq.popleft()
    for v in g[u]:
        if C[v] == C[u]:
            nibu = False
            break
        if C[v] >= 0:
            continue
        C[v] = 1 - C[u]
        dq.append(v)
    if not nibu:
        break

print(C.count(0) * C.count(1) - M if nibu else N*(N-1)//2-M)