from sortedcontainers import SortedList

N, K = map(int,input().split())
P = list(map(int,input().split()))

SL = SortedList(P[:K-1])

for i in range(K-1,N):
    SL.add(P[i])
    print(SL[-K])