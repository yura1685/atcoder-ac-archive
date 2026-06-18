from sortedcontainers import SortedList
N, K, Q = map(int,input().split())
A = [0] * N
S = SortedList([0]*N)
ans = 0
for _ in range(Q):
    x, q = map(int,input().split())
    q = -q
    x -= 1
    p = A[x]
    A[x] = q 
    # p -> q
    if S.index(p) < K:
        S.discard(p)
        ans -= p
        S.add(q)
        if S.index(q) < K:
            ans += q 
        else:
            ans += S[K-1]
    else:
        S.discard(p)
        S.add(q)
        if S.index(q) < K:
            ans -= S[K]
            ans += q
    print(-ans)