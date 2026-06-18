from sortedcontainers import SortedList

N, K = map(int,input().split())
P = list(map(int,input().split()))
Q = [-1] * N
for i in range(N): Q[P[i]-1] = i

SL = SortedList(Q[:K])

ans = SL[-1] - SL[0]
for i in range(K,N):
    SL.discard(Q[i-K])
    SL.add(Q[i])
    ans = min(ans,SL[-1] - SL[0])

print(ans)