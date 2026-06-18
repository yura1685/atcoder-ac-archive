from sortedcontainers import SortedList

N, K = map(int,input().split())
H = list(map(int,input().split()))
SL = SortedList(H[:K])

ans = SL[K-1] - SL[0]
for i in range(N-K):
    lost, new = H[i], H[i+K]
    SL.discard(lost)
    SL.add(new)
    ans = max(ans, SL[K-1] - SL[0])

print(ans)