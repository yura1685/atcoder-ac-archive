N, M = map(int,input().split())

Ball = [1]*N
red  = [False]*N
red[0] = True

for _ in range(M):
    x, y = map(int,input().split())
    x, y = x-1, y-1
    Ball[x] -= 1
    Ball[y] += 1
    if red[x]:
        red[y] = True
    if Ball[x] == 0:
        red[x] = False

print(sum(red))