from collections import deque

M = int(input())
g = [[] for _ in range(9)]
for _ in range(M):
    u, v = map(int,input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

P_ = [int(x)-1 for x in input().split()]
P = [8] * 9
for i in range(8): P[P_[i]] = i

def hash(L):
    res = 0
    for i in range(9):
        res += L[i] * 10**i
    return res

s = set([hash(P)])
dq = deque([(P,0)])
while dq:
    P, step = dq.popleft()
    H = hash(P)
    if H == 876543210:
        exit(print(step))
    u = P.index(8)
    for v in g[u]:
        Q = P.copy()
        Q[v], Q[u] = Q[u], Q[v]
        H = hash(Q)
        if H not in s:
            s.add(H)
            dq.append((Q,step+1))

print(-1)