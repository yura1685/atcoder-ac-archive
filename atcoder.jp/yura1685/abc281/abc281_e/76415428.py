from sortedcontainers import SortedList

N, M, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
SL = SortedList(A[:M])
S = sum(SL[:K])

ans = []
for i in range(N-M+1):
    ad = A[i+M]
    re = A[i]
    if SL.bisect_right(ad) >= K:
        SL.add(ad)
    else:
        SL.add(ad)
        S += ad - SL[K]
    if SL.bisect_right(re) >= K + 1:
        SL.discard(re)
    else:
        SL.discard(re)
        S += SL[K-1] - re
    ans.append(S)

print(*ans)