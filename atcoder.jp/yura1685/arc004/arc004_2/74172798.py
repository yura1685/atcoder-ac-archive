N = int(input())
S, M = 0, 0
for _ in range(N):
    d = int(input())
    S += d
    M = max(M, d)

print(S)
print(max(2*M - S, 0))