from collections import deque

H, W = map(int,input().split())
glid = [['=']*(W+2)] + [list('='+input()+'=') for _ in range(H)] + [['=']*(W+2)]
c = [(-1,0),(0,-1),(0,1),(1,0)]

check = [[0]*(W+2) for _ in range(H+2)]

dic = {'.':'#', '#':'.'}

ans = 0
for i in range(1,H+1):
    for j in range(1,W+1):
        if check[i][j] == 0:
            check[i][j] = 1
        else:
            continue
        hoge = glid[i][j]
        d = deque([(i,j)])
        while d:
            h, w = d.popleft()
            for dh, dw in c:
                if glid[h+dh][w+dw] == dic[glid[h][w]] and check[h+dh][w+dw] == 0:
                    d.append((h+dh,w+dw))
                    check[h+dh][w+dw] = 1
                    hoge += glid[h+dh][w+dw]

        ans += hoge.count('.') * hoge.count('#')

print(ans)