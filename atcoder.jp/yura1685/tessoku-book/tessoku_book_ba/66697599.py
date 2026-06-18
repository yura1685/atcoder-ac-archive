import heapq

Q = int(input())

T = []

for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        heapq.heappush(T,int(q[1]))
    if q[0] == '2':
        print(T[0])
    if q[0] == '3':
        heapq.heappop(T)