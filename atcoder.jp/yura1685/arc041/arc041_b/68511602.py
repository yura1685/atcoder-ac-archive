N, M = map(int,input().split())
ameba = [list(map(int,list(input()))) for _ in range(N)]

ans = [[0]*M for _ in range(N)]

for i in range(N-1):
    for j in range(M):
        if ameba[i][j] > 0:
            A = ameba[i][j]
            ans[i+1][j] += A
            ameba[i][j] = 0
            ameba[i+1][j-1] -= A
            ameba[i+1][j+1] -= A
            ameba[i+2][j] -= A

for i in ans:
    l = ''
    for s in i:
        l += str(s)
    print(l)