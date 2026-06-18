import heapq

N = int(input())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

hq = [(T[i],i) for i in range(N)]
heapq.heapify(hq)

c = [0]*N
ok = 0

while ok < N:
    t, m = heapq.heappop(hq)
    if c[m] == 0:
        c[m] = t
        ok += 1
        heapq.heappush(hq,(t + S[m],(m+1) % N))

for i in c:
    print(i)
