N, M = map(int,input().split())
L = [[0]*9 for _ in range(N+1)]
L[0] = [i % M for i in range(1,10)]
for i in range(1,N+1):
    for j in range(9):
        L[i][j] = (10*L[i-1][j] + j + 1) % M

flag = 0
for i in range(N-1,-1,-1):
    for j in range(8,-1,-1):
        if L[i][j] == 0:
            n, m = i, j
            flag = 1
            break
    if flag:
        break

if not flag: exit(print(-1))

print((m+1)*(pow(10,n+1)-1)//9)