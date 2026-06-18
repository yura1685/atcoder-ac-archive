from sortedcontainers import SortedList

N, K = map(int,input().split())
X = list(map(int,input().split()))

SL = SortedList()
for i in range(K-1):
    SL.add((X[i],i+1))

for i in range(K-1,N):
    SL.add((X[i],i+1))
    print(SL[K-1][1])