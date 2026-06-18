from sys import setrecursionlimit
setrecursionlimit(10**8)

N, M = map(int,input().split())
g1 = [[] for _ in range(N)]
g2 = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int,input().split())
    A, B = A-1, B-1
    g1[A].append(B)
    g2[B].append(A)

cnt = 1
dis = []
check = [0]*N
def dfs1(u):
    global cnt
    check[u] = 1
    for v in g1[u]:
        if check[v] == 0:
            dfs1(v)
    dis.append((u,cnt))
    cnt += 1

for i in range(N):
    if check[i] == 0:
        dfs1(i)



def dfs2(u):
    res = 1
    check[u] = 0
    for v in g2[u]:
        if check[v]:
            res += dfs2(v)
    return res

ans = 0
for u, d in dis[::-1]:
    if check[u]:
        n = dfs2(u)
        ans += n*(n-1)//2

print(ans)