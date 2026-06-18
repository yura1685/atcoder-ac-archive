X = input()
Y = input()
N, M = len(X), len(Y)

ac_x = [[0] * 26 for _ in range(N + 1)]
ac_y = [[0] * 26 for _ in range(M + 1)]
for i in range(N):
    x = X[i]
    for j in range(26):
        ac_x[i+1][j] = ac_x[i][j]
    ac_x[i+1][ord(x) - 97] += 1
for i in range(M):
    y = Y[i]
    for j in range(26):
        ac_y[i+1][j] = ac_y[i][j]
    ac_y[i+1][ord(y) - 97] += 1

inf = 10 ** 18 + 1685
Len = [0, N, M]
count = [[], ac_x[N], ac_y[M]]
while 1:
    Len.append(Len[-1] + Len[-2])
    count.append([count[-1][i] + count[-2][i] for i in range(26)])
    if Len[-1] >= inf:
        break

LL = len(Len) - 1
# Snの先頭k文字に含まれる文字cの個数
def f(n, k, c) -> int:
    if k == 0: return 0
    if n == 1: return ac_x[min(k, N)][c]
    if n == 2: return ac_y[min(k, M)][c]
    if k >= Len[n]: return count[n][c]
    if k <= Len[n-1]: return f(n-1, k, c)
    else: return count[n-1][c] + f(n-2, k-Len[n-1], c)

Q = int(input())
for _ in range(Q):
    q = input().split()
    L, R = int(q[0]), int(q[1])
    C = ord(q[2]) - 97
    print(f(LL, R, C) - f(LL, L-1, C))