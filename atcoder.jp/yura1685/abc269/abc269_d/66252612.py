from collections import deque

N = int(input())

hexa = [tuple(map(int,input().split())) for _ in range(N)]
check = [0]*N
ans = 0

a = [(-1,-1),(-1,0),(0,-1),(0,1),(1,0),(1,1)]

for i in range(N):
    if check[i] == 0:
        ans += 1
        d = deque([(hexa[i][0],hexa[i][1])])
        while d != deque():
            x, y = d.pop()
            check[hexa.index((x,y))] = 1
            for dx, dy in a:
                if (x+dx,y+dy) in hexa and check[hexa.index((x+dx,y+dy))] == 0:
                    check[hexa.index((x+dx,y+dy))] = 1
                    d.append((x+dx,y+dy))
print(ans)