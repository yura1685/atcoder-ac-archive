from sortedcontainers import SortedList

S = SortedList()

Q = int(input())
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        S.add(q[1])
    if q[0] == 2:
        x, k = q[1], q[2]
        i = S.bisect_right(x)
        if i < k:
            print(-1)
        else:
            print(S[i-k])
    if q[0] == 3:
        x, k = q[1], q[2]
        i = S.bisect_left(x)
        if i + k > len(S):
            print(-1)
        else:
            print(S[i+k-1])