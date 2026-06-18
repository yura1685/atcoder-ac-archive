from atcoder.dsu import DSU

N, M = map(int,input().split())
bridge = []

for _ in range(M):
    c = tuple(map(int,input().split()))
    bridge.append(c)

ans = 0
for bomb in bridge:
    dsu = DSU(N+1)
    for x in bridge:
        if x != bomb:
            dsu.merge(x[0],x[1])
    if len(dsu.groups()) >= 3:
        ans += 1

print(ans)