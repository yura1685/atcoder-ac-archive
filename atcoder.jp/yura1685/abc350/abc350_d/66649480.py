from atcoder.dsu import DSU

N, M = map(int,input().split())
d = DSU(N+1)

for _ in range(M):
    A, B = map(int,input().split())
    d.merge(A,B)

ans = 0
for i in d.groups():
    if i == [0]:
        continue
    n = len(i)
    ans += n*(n-1)//2

print(ans-M)