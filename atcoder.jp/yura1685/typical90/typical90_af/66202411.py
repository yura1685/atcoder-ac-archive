from itertools import permutations

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
M = int(input())
no_friend = [[0]*N for _ in range(N)]
for _ in range(M):
    x, y = map(int,input().split())
    no_friend[x-1][y-1] = 1
    no_friend[y-1][x-1] = 1

l = [i for i in range(N)]

ans = 10**10
for v in permutations(l):
    if all([no_friend[v[i]][v[i+1]] == 0 for i in range(N-1)]):
        yura = 0
        for c in range(N):
            r = v[c]
            yura += A[r][c]
        ans = min(ans, yura)

if ans == 10**10:
    print(-1)
else:
    print(ans)