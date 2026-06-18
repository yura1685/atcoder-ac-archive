from collections import deque

N, M = map(int,input().split())
ice = [list(input()) for _ in range(N)]

ice[1][1] = '2'
check = [[False]*M for _ in range(N)]
check[1][1] = True
d = deque([(1,1)])
c = [(-1,0),(0,-1),(0,1),(1,0)]

while d:
    H, W = d.popleft()
    for dh, dw in c:
        h, w = H, W
        while ice[h+dh][w+dw] != '#':
            h, w = h+dh, w+dw
            if ice[h][w] == '.':
                ice[h][w] = '1'
        if ice[h][w] != '2':
            ice[h][w] = '2'
            if check[h][w] == False:
                check[h][w] = True
                d.append((h,w))
                
ans = 0
for i in ice:
    ans += i.count('1') + i.count('2')
print(ans)