from atcoder.dsu import DSU

N, M = map(int,input().split())

fr = DSU(N+1)
for _ in range(M):
    A, B = map(int,input().split())
    fr.merge(A,B)

ans = 0
for p in fr.groups():
    ans = max(ans,len(p))

print(ans)