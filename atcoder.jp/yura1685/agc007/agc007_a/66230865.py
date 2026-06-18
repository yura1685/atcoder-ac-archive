H, W = map(int,input().split())

glid = [list('.'+input()+'.') for _ in range(H)]
glid = [['.']*(W+2)] + glid + [['.']*(W+2)]
h, w = 1, 1

while (h,w) != (H,W):
    glid[h][w] = '.'
    if glid[h+1][w] == glid[h][w+1]:
        print('Impossible')
        exit()
    if glid[h-1][w] == '#' or glid[h][w-1] == '#':
        print('Impossible')
        exit()
    if glid[h][w+1] == '#':
        w += 1
    elif glid[h+1][w] == '#':
        h += 1

if glid[H-1][W] == glid[H][W-1] =='.':
    print('Possible')
else:
    print('Impossible')