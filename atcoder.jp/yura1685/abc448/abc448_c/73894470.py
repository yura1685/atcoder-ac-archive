I = input().split()
N, Q = int(I[0]), int(I[1])
A = list(map(int, input().split()))
minA = sorted(A)[:6]

for _ in range(Q):
    K = int(input())
    B = list(map(int, input().split()))
    s = minA.copy()
    for b in B:
        if A[b-1] in s:
            s.pop(s.index(A[b-1]))
    print(s[0])