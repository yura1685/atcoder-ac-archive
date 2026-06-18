import heapq

Q = int(input())
P = []
heapq.heapify(P)
S = 0
for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        heapq.heappush(P,int(q[1])-S)
    if q[0] == '2':
        S += int(q[1])
    if q[0] == '3':
        x = heapq.heappop(P)
        print(x+S)