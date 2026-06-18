from collections import deque

N, D = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(N)]

virus = [0] * N
virus[0] = 1

D_squared = D ** 2 

def distance_squared(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

queue = deque([0])

while queue:
    current = queue.popleft()
    for i in range(N):
        if virus[i] == 0 and distance_squared(points[current], points[i]) <= D_squared:
            virus[i] = 1
            queue.append(i)

for status in virus:
    print('Yes' if status == 1 else 'No')
