from atcoder.dsu import DSU

N, M = map(int,input().split())
E = []
for _ in range(M):
    A, B, C = map(int,input().split())
    E.append((C,A-1,B-1))
E.sort(reverse=True)

uf = DSU(N)

ans = 0
while E:
    c, a, b = E.pop()
    if uf.same(a,b): continue
    uf.merge(a,b)
    ans += c 

print(ans)