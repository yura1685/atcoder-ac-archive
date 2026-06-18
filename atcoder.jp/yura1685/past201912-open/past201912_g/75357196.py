N = int(input())
A = []
for i in range(N-1):
    a = [0] * (i+1) + list(map(int, input().split()))
    A.append(a)
A.append([0] * N)
for i in range(N):
    for j in range(i):
        A[i][j] = A[j][i]

ans = - 10 ** 8
for n in range(3 ** N):
    M = 0
    g0, g1, g2 = [], [], []
    for i in range(N):
        mod = (n // 3 ** i) % 3
        if mod:
            if mod - 1:
                g2.append(i)
            else:
                g1.append(i)
        else:
            g0.append(i)
    for lst in [g0, g1, g2]:
        if len(lst) > 1:
            for i in range(len(lst)):
                for j in range(i+1, len(lst)):
                    M += A[lst[i]][lst[j]]
    ans = max(ans, M)

print(ans)