N, C, K = map(int,input().split())
T = sorted(int(input()) for _ in range(N))

B, S, L = 0, 0, 0
for t in T:
    if S + K < t or L == 0:
        S, L = t, C-1
        B += 1
    else:
        L -= 1
print(B)