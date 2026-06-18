N, M = map(int,input().split())
d = {}

for _ in range(M):
    a, b = map(int,input().split())
    if d.get(a) == None:
        d[a] = {b}
    else:
        d[a].add(b)
    if d.get(b) == None:
        d[b] = {a}
    else:
        d[b].add(a)

c = d[1]
for s in c:
    if N in d[s]:
        print('POSSIBLE')
        exit()
print('IMPOSSIBLE')