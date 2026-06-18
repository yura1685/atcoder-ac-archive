N, M = map(int, input().split())
C = list(map(int, input().split()))
S = sum(C)
for _ in range(N):
    A, B = map(int, input().split())
    A -= 1
    if C[A] < B:
        C[A] = 0
    else:
        C[A] -= B

print(S - sum(C))