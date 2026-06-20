from sortedcontainers import SortedSet

N, C, Q = map(int, input().split())
A = list(map(int, input().split()))
S = [SortedSet([N+1]) for _ in range(C+1)]
for i, a in enumerate(A): S[a].add(i+1)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        p, x = q[1], q[2]
        a = A[p-1]
        S[a].discard(p)
        A[p-1] = x
        S[x].add(p)
    else:
        l, r, d = q[1], q[2], q[3]
        now = l
        ans = S[0].bisect_right(r) - S[0].bisect_left(l)
        while d > 0:
            nxtmin = r + 1
            cost = -1
            for i in range(1, d + 1):
                nxt = S[i][S[i].bisect_left(now)]
                if nxt < nxtmin:
                    nxtmin = nxt
                    cost = i
            if nxtmin <= r:
                ans += 1
                d -= cost
                now = nxtmin + 1
            else:
                break
        print(ans)