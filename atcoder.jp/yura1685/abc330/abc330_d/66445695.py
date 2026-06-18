N = int(input())
glid = [input() for _ in range(N)]
rota = list(zip(*glid))

oglid = [glid[i].count('o')-1 for i in range(N)]
orota = [rota[j].count('o')-1 for j in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        if glid[i][j] == rota[j][i] == 'o':
            ans += oglid[i] * orota[j]

print(ans)