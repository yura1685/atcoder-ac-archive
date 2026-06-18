H, W = map(int,input().split())
glid = [['.']*(W+2)]
for _ in range(H):
    x = '.' + input() + '.'
    glid.append(list(x))
glid.append(['.']*(W+2))

def d(h,w):
    return glid[h][w] == '#'

c = [-1,0,1]

for i in range(1,H+1):
    for j in range(1,W+1):
        bomb = 0
        if glid[i][j] == '.':
            for sex1 in c:
                for sex2 in c:
                    bomb += d(i+sex1,j+sex2)
            glid[i][j] = str(bomb)

for h in range(1,H+1):
    s = glid[h][1:-1]
    print(''.join(s))