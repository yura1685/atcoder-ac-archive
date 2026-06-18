L = ['']*4
for i in range(4):
    L[i] = list(map(int,input().split()))
for i in range(4):
    for j in range(3):
        if L[i][j] == L[i][j+1]:
            print('CONTINUE');exit()

for j in range(4):
    for i in range(3):
        if L[i][j] == L[i+1][j]:
            print('CONTINUE');exit()

print('GAMEOVER')