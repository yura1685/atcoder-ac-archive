N = int(input())
d = {'-':'-', 'W':'L', 'L':'W', 'D':'D'}
A = [input() for _ in range(N)]
for i in range(N):
    for j in range(N):
        if A[i][j] != d[A[j][i]]:
            print('incorrect')
            exit()
print('correct')