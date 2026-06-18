from atcoder.dsu import DSU

N, M = map(int,input().split())
dsu = DSU(2*N)
# ロープi の赤を2i, 青を2i+1とする．

loop = 0
for _ in range(M):
    q = input().split()
    A = int(q[0]) - 1
    B = 2*A + (q[1] == 'B')
    C = int(q[2]) - 1
    D = 2*C + (q[3] == 'B')
    dsu.merge(2*A,2*A+1)
    dsu.merge(2*C,2*C+1)
    if dsu.same(B,D):
        loop += 1
    dsu.merge(B,D)

S, T = 0, 0
for lst in dsu.groups():
    if len(lst) == 1:
        S += 1
    else:
        T += 1

print(loop, S//2 + (T-loop))