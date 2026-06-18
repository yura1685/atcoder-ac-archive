from atcoder.dsu import DSU

N, M = map(int,input().split())
d = [0]*(N+1)
g = DSU(N+1)

for _ in range(M):
    A, B = map(int,input().split())
    d[A] += 1
    d[B] += 1
    g.merge(A,B)

ans = 0
for bbn in g.groups():
    cnt = 0
    for c in bbn:
        cnt += d[c]
    ans += cnt//2 - len(bbn) + 1

print(ans)