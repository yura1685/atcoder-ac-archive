H, W = map(int,input().split())
glid = ['']*H
for i in range(H):
    glid[i] = input()

for i in range(H):
    for j in range(W):
        if glid[i][j] == '#':
            if j == 0:
                if i == 0:
                    if glid[1][0] == glid[0][1] == '.':
                        print('No')
                        exit()
                elif i == H-1:
                    if glid[H-2][0] == glid[H-1][1] == '.':
                        print('No')
                        exit()
                else:
                    if glid[i-1][0] == glid[i+1][0] == glid[i][1] == '.':
                        print('No')
                        exit()
            elif j == W-1:
                if i == 0:
                    if glid[0][W-2] == glid[1][W-1] == '.':
                        print('No')
                        exit()
                elif i == H-1:
                    if glid[H-1][W-2] == glid[H-2][W-1] == '.':
                        print('No')
                        exit()
                else:
                    if glid[i-1][W-1] == glid[i+1][W-1] == glid[i][W-2] == '.':
                        print('No')
                        exit()
            else:
                if i == 0:
                    if glid[0][j-1] == glid[0][j+1] == glid[1][j] == '.':
                        print('No')
                        exit()
                elif i == H-1:
                    if glid[H-1][j-1] == glid[H-1][j+1] == glid[H-2][j] == '.':
                        print('No')
                        exit()
                else:
                    if glid[i-1][j] == glid[i+1][j] == glid[i][j-1] == glid[i][j+1] == '.':
                        print('No')
                        exit()
print('Yes')