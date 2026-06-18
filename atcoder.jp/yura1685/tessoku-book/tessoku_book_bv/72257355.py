N = int(input())
P = [list(map(int,input().split())) for _ in range(N)]
X, Y = [-1] * N, [-1] * N
for i in range(N):
    for j in range(N):
        if P[i][j]:
            X[i] = P[i][j]
            Y[j] = P[i][j]

def solve(L):
    res = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if L[i] > L[j]:
                res += 1
    return res

print(solve(X) + solve(Y))