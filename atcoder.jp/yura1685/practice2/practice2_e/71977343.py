from atcoder.mincostflow import MCFGraph

N, K = map(int,input().split())
s = 2*N
t = s + 1
g = MCFGraph(t+1)
A = [list(map(int,input().split())) for _ in range(N)]
B = 1 << 40
# 0~N-1: 行, N~2N-1: 列, 2N: スタート, 2N+1: ゴール
for i in range(N):
    g.add_edge(s, i, K, 0)
    g.add_edge(i+N, t, K, 0)
    for j in range(N):
        g.add_edge(i, j+N, 1, B-A[i][j])

g.add_edge(s, t, N*K, B)
cost = g.flow(s, t, N*K)[1]
print(N*K*B - cost)

ans = [['.']*N for _ in range(N)]

for e in g.edges():
    if e.src == s or e.dst == t or e.flow == 0:
        continue
    i, j = e.src, e.dst-N
    ans[i][j] = 'X'

for a in ans:
    print(''.join(a))