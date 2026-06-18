from collections import deque

H, W = map(int,input().split())
glid = [list('#'+input()+'#') for _ in range(H)]
glid = [['#']*(W+2)] + glid + [['#']*(W+2)]

d = deque()
for i in range(H+2):
    for j in range(W+2):
        if glid[i][j] == 'E':
            d.append((i,j))

while d != deque([]):
    i, j = d[0]
    if glid[i-1][j] == '.':
        glid[i-1][j] = 'v'
        d.append((i-1,j))
    if glid[i][j-1] == '.':
        glid[i][j-1] = '>'
        d.append((i,j-1))
    if glid[i][j+1] == '.':
        glid[i][j+1] = '<'
        d.append((i,j+1))
    if glid[i+1][j] == '.':
        glid[i+1][j] = '^'
        d.append((i+1,j))
    d.popleft()

for row in glid[1:-1]:
    print(''.join(row[1:-1]))