from math import gcd

N = int(input())

city = [tuple(map(int,input().split())) for _ in range(N)]
ans = set()

for i in range(N-1):
    for j in range(i+1,N):
        x1, y1 = city[i]
        x2, y2 = city[j]
        x, y = x2-x1, y2-y1
        g = gcd(x,y)
        ans.add((x//g, y//g))
        ans.add((-x//g,-y//g))

print(len(ans))