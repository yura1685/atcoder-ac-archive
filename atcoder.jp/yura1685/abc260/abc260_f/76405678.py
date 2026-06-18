S, T, M = map(int, input().split())
G = [[] for _ in range(S)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u-1].append(v)

M = [[-1]*T for _ in range(T)]
for u in range(1, S+1):
    for x in G[u-1]:
        for y in G[u-1]:
            if x <= y:
                continue
            if M[x - S - 1][y - S - 1] == -1:
                M[x - S - 1][y - S - 1] = u
            else:
                v = M[x - S - 1][y - S - 1]
                print(u, x, y, v)
                exit()
print(-1)