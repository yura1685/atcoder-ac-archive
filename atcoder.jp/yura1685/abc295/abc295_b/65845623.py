R, C = map(int,input().split())
hoge = [['y']*(C+18) for _ in range(9)]
glid = []
for i in range(R):
    glid.append(list('y'*9 + input() + 'y'*9))
glid = hoge + glid + hoge

for r in range(9,9+R):
    for c in range(9,9+C):
        if glid[r][c] in '123456789':
            bomb = int(glid[r][c])
            for h in range(r-bomb,r+bomb+1):
                haba = bomb - abs(r-h)
                for w in range(c-haba, c+haba+1):
                    if glid[h][w] == '#':
                        glid[h][w] = '.'
            glid[r][c] = '.'

for i in glid[9:-9]:
    j = i[9:-9]
    print(''.join(j))