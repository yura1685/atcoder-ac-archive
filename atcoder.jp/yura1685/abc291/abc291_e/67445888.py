from collections import deque

N, M = map(int,input().split())
g = [[] for _ in range(N)] # 有向グラフ
c = [0]*N # 頂点iが終点となっているパスの個数

for _ in range(M):
    x, y = map(int,input().split())
    x, y = x-1, y-1
    g[x].append(y)
    c[y] += 1

d = deque()
ans = [0]*N

for i in range(N): # まず、最初のところ
    if c[i] == 0:
        d.append(i)

if len(d) > 1:
    print('No')
    exit()

num = 1
while d:
    u = d.popleft()
    ans[u] = num
    num += 1
    cnt = 0
    for v in g[u]:
        c[v] -= 1
        if c[v] == 0:
            d.append(v)
            cnt += 1
    if cnt > 1:
        print('No')
        exit()

print('Yes')
print(*ans)