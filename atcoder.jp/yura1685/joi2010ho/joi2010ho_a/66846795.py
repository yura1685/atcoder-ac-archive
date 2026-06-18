from itertools import accumulate

n, m = map(int,input().split())
a = [int(input()) for _ in range(n-1)]

road = [0] + list(accumulate(a))

now = 0
walk = 0

for i in range(m):
    to = now + int(input())
    walk = (walk + abs(road[to]-road[now])) % 10**5
    now = to

print(walk)