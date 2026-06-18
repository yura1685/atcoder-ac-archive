N, L, R = map(int,input().split())
M, idx = -1, -1
P = list(map(int,input().split()))

for i in range(N):
    if L <= P[i] <= R:
        if M < P[i]:
            M = P[i]
            idx = i + 1

print(idx)