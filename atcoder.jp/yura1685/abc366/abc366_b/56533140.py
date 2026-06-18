N = int(input())
S = []
M = 0
for i in range(N):
    s = input()
    M = max(M,len(s))
    S.append(s)

U = []
for i in S:
    i = i + '*'*(M-len(i))
    U.append(i)

W = []
for i in range(M):
    a = U[-1][i]
    for j in range(N-1):
        a += U[N-j-2][i]
    W.append(a)


for i in W:
    while i[-1] == '*':
        i = i[:-1]
    print(i)    