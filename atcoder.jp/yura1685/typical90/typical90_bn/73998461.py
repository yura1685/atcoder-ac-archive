N = int(input())
X = []
for _ in range(N):
    L, R = map(int, input().split())
    X.append((L, R))

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        Li, Ri = X[i]
        Lj, Rj = X[j]
        cnt = 0
        for n in range(Li, Ri+1):
            if n <= Lj:
                continue
            cnt += min(n, Rj+1) - Lj
        ans += cnt / ((Ri - Li + 1) * (Rj - Lj + 1))

print(ans)