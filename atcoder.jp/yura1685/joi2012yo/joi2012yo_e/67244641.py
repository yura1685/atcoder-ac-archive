from collections import deque

W, H = map(int,input().split())

glid = [[0]+list(map(int,input().split()))+[0] for _ in range(H)]
glid = [[0]*(W+2)] + glid + [[0]*(W+2)]
ceven = [(-1,-1),(-1,0),(0,-1),(0,1),(1,-1),(1,0)]
codd  = [(-1,0),(-1,1),(0,-1),(0,1),(1,0),(1,1)]

check = [[0]*(W+2) for _ in range(H+2)]
check[0][0] = 1

ill = 0
d = deque([(0,0)])
while d:
    h, w = d.popleft()
    if h % 2 == 0:
        c = ceven
    else:
        c = codd
    for dh, dw in c:
        hh, ww = h+dh, w+dw
        if not (0 <= hh <= H+1 and 0 <= ww <= W+1):
            continue
        if glid[hh][ww] == 1:
            ill += 1
        else:
            if check[hh][ww] == 0:
                d.append((hh,ww))
                check[hh][ww] = 1

print(ill)