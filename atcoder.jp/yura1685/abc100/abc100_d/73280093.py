from itertools import product

N, M = map(int,input().split())
cake = []
for _ in range(N):
    x, y, z = map(int,input().split())
    cake.append(((x,y,z),(-x,-y,-z)))

ans = 0
for a, b, c in product([0,1],repeat=3):
    L = []
    for xyz in cake:
        L.append(xyz[a][0]+xyz[b][1]+xyz[c][2])
    L.sort(reverse=True)
    ans = max(ans, sum(L[:M]))

print(ans)