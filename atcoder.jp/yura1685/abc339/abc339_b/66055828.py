H, W, N = map(int,input().split())
houkou = 0

glid = [['.']*W for _ in range(H)]
x, y = 0, 0

for _ in range(N):
    if glid[x][y] == '.':
        glid[x][y] = '#'
        houkou = (houkou+1) % 4
    elif glid[x][y] == '#':
        glid[x][y] = '.'
        houkou = (houkou-1) % 4
    if houkou == 0:
        x = (x-1) % H
    if houkou == 1:
        y = (y+1) % W
    if houkou == 2:
        x = (x+1) % H
    if houkou == 3:
        y = (y-1) % W

for i in glid:
    print(''.join(i))