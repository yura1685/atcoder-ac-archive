from sys import setrecursionlimit
setrecursionlimit(10**8)

N = int(input())
A = input()

X = [[] for _ in range(N+1)]
X[0] = [int(a) for a in A]

for i in range(1,N+1):
    for j in range(3**(N-i)):
        if sum(X[i-1][3*j:3*j+3]) >= 2:
            X[i].append(1)
        else:
            X[i].append(0)

cnt = [[-1]*3**i for i in range(N,-1,-1)]

def dfs(i, j):
    if i == 0:
        return 1
    x, y, z = X[i-1][3*j], X[i-1][3*j+1], X[i-1][3*j+2]
    S = x+y+z
    if X[i][j] == 0:
        if S == 0:
            koho = [dfs(i-1,3*j), dfs(i-1,3*j+1), dfs(i-1,3*j+2)]
            cnt[i][j] = sum(koho) - max(koho)
            return cnt[i][j]
        else:
            koho = []
            for k in range(3):
                if X[i-1][3*j+k] == 1:
                    continue
                koho.append(dfs(i-1,3*j+k))
            cnt[i][j] = min(koho)
            return cnt[i][j]
    else:
        if S == 3:
            koho = [dfs(i-1,3*j), dfs(i-1,3*j+1), dfs(i-1,3*j+2)]
            cnt[i][j] = sum(koho) - max(koho)
            return cnt[i][j]
        else:
            koho = []
            for k in range(3):
                if X[i-1][3*j+k] == 0:
                    continue
                koho.append(dfs(i-1,3*j+k))
            cnt[i][j] = min(koho)
            return cnt[i][j]

print(dfs(N,0))