from bisect import bisect_left, bisect_right

N = int(input())
g = [[] for _ in range(N)]
P = [int(x) - 1 for x in input().split()]
for u in range(1,N):
    v = P[u-1]
    g[u].append(v)
    g[v].append(u)

depth = [-1] * (N + 1)
In, Out = [-1] * (N + 1), [-1] * (N + 1)
step = 1
stack = [(0, -1, True)]
while stack:
    u, f, b = stack.pop()
    if b == True:
        depth[u] = depth[f] + 1
        stack.append((u, f, False))
        In[u] = step
        for v in g[u]:
            if v == f:
                continue
            stack.append((v, u, True))
    else:
        Out[u] = step
    step += 1

Dep = [[] for _ in range(N+1)]
for u in range(N):
    d = depth[u]
    Dep[d].append(In[u])
    Dep[d].append(Out[u])
    
for D in Dep:
    D.sort()

Q = int(input())
for _ in range(Q):
    U, D = map(int, input().split())
    U -= 1
    R = bisect_right(Dep[D], Out[U])
    L = bisect_left(Dep[D], In[U])
    print((R - L) // 2)