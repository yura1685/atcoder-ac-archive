N = int(input())
glid = [input() for _ in range(N)]
rota = list(zip(*glid))

oglid = [-1]*N
orota = [-1]*N

for i in range(N):
    for j in range(N):
        if glid[i][j] == 'o':
            oglid[i] += 1
            orota[j] += 1

ans = 0
for i in range(N):
    for j in range(N):
        if glid[i][j] == rota[j][i] == 'o':
            ans += oglid[i] * orota[j]

print(ans)