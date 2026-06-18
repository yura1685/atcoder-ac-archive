N, M = map(int,input().split())
glid = ['']*N
for i in range(N):
    glid[i] = input()
for i in range(0,N-8):
    for j in range(0,M-8):
        if glid[i][j:j+4] == '###.':
            if glid[i+1][j:j+4] == '###.':
                if glid[i+2][j:j+4] == '###.':
                    if glid[i+3][j:j+4] == '....':
                        if glid[i+5][j+5:j+9] == '....':
                            if glid[i+6][j+5:j+9] == '.###':
                                if glid[i+7][j+5:j+9] == '.###':
                                    if glid[i+8][j+5:j+9] == '.###':
                                        print(i+1,j+1)

