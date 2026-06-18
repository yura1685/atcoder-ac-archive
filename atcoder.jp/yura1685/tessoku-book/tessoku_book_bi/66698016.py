N, M = map(int,input().split())

g = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int,input().split())
    g[A].append(B)
    g[B].append(A)

for i in range(1,N+1):
    print(str(i)+':', set(g[i]) if g[i] else '{}')