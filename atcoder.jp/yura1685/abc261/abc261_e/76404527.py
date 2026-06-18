N, C = map(int, input().split())
Q = []
for _ in range(N):
    T, A = map(int, input().split())
    Q.append((T, A))

f = [[(0, 1) for _ in range(N+1)] for _ in range(30)]
for bit in range(30):
    for i in range(N):
        a, b = f[bit][i]
        T, A = Q[i]
        A = (A >> bit) & 1
        if T == 1:
            f[bit][i+1] = (a & A, b & A)
        if T == 2:
            f[bit][i+1] = (a | A, b | A)
        if T == 3:
            f[bit][i+1] = (a ^ A, b ^ A)

ans = [[] for _ in range(N)]
for bit in range(30):
    c = (C >> bit) & 1
    for i in range(N):
        c = f[bit][i+1][c]
        ans[i].append(str(c))

for L in ans:
    L.reverse()
    n = ''.join(L)
    print(int(n, 2))