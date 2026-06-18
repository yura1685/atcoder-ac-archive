def solve():
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort(); B.sort(reverse=True)
    a, b = 0, 0
    S = 0
    while a < N:
        if A[a] + B[b] >= M:
            S += A[a] + B[b] - M
            a, b = a + 1, b + 1
        else:
            S += A[a]
            a += 1
    print(S+sum(B[b:]))

Q = int(input())
for _ in range(Q):
    solve()