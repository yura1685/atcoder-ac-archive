from collections import deque

N = int(input())
g = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

def solve(u):
    dq = deque([u])
    check = [0] * N
    check[u] = 1
    while dq:
        u = dq.popleft()
        last = u
        for v in g[u]:
            if check[v] == 0:
                check[v] = 1
                dq.append(v)
    return last

u = solve(0)
v = solve(u)

print(u+1, v+1)