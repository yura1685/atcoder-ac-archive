from sortedcontainers import SortedSet

N = 1 << 20
A = [-1] * N
S = SortedSet(range(N))
Q = int(input())
for _ in range(Q):
    t, x = map(int,input().split())
    if t == 1:
        h = x % N
        idx = S.bisect_left(h)
        if idx == len(S):
            h = S.pop(0)
            A[h] = x
        else:
            h = S[idx]
            S.discard(h)
            A[h] = x
    else:
        print(A[x % N])