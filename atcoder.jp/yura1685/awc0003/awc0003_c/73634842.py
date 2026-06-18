I = input().split()
N, K = int(I[0]), int(I[1])
X:list[tuple[int, int, int]] = []
for _ in range(N):
    I = input().split()
    a, b = int(I[0]), int(I[1])
    X.append((b-a, a, b))
X.sort()
ans = 0
for i in range(N):
    if i < K:
        ans += X[i][2]
    else:
        ans += X[i][1]

print(ans)