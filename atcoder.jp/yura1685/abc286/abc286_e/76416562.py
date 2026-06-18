from collections import deque

inf = 10 ** 18
N = int(input())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]
G = [[(inf, inf) for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if S[i][j] == 'Y':
            G[i][j] = (1, A[i])

for j in range(N):
    for i in range(N):
        for k in range(N):
            s_ij, v_ij = G[i][j]
            s_jk, v_jk = G[j][k]
            s_ik, v_ik = G[i][k]
            if s_ij + s_jk < s_ik:
                G[i][k] = (s_ij + s_jk, v_ij + v_jk)
            elif s_ij + s_jk == s_ik:
                G[i][k] = (s_ij + s_jk, max(v_ij + v_jk, v_ik))

Q = int(input())
for _ in range(Q):
    U, V = map(int, input().split())
    U, V = U-1, V-1
    s, v = G[U][V]
    v += A[V]
    if s < inf:
        print(s, v)
    else:
        print('Impossible')