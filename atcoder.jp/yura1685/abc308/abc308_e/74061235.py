def mex(x,y,z):
    s = set([x,y,z])
    m = 0
    while m in s:
        m += 1
    return m

N = int(input())
A = list(map(int,input().split()))
S = input()
M = [[0]*3 for _ in range(N+1)]
X = [[0]*3 for _ in range(N+1)]
for i in range(N):
    M[i+1][0] = M[i][0]
    M[i+1][1] = M[i][1]
    M[i+1][2] = M[i][2]
    if S[i] == 'M':
        M[i+1][A[i]] += 1

    X[N-1-i][0] = X[N-i][0]
    X[N-1-i][1] = X[N-i][1]
    X[N-1-i][2] = X[N-i][2]
    if S[N-1-i] == 'X':
        X[N-1-i][A[N-1-i]] += 1

ans = 0
for i in range(N):
    if S[i] == 'E':
        a = A[i]
        for j in range(3):
            for k in range(3):
                ans += M[i][j] * X[i][k] * mex(a,j,k)

print(ans)