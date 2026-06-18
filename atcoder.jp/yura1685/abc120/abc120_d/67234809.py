from atcoder.dsu import DSU

N, M = map(int,input().split())
line = [tuple(map(int,input().split())) for _ in range(M)]
line.reverse()

g = DSU(N+1)

ans = [N*(N-1)//2]
for A, B in line:
    if g.same(A,B):
        X = 0
    else:
        X = g.size(A) * g.size(B)
    g.merge(A,B)
    ans.append(ans[-1]-X)

for i in range(M):
    print(ans[M-i-1])