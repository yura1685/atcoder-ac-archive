H, W = map(int,input().split())
glid = []
for i in range(H):
    glid.append(input())

for i in range(H):
    if '#' in glid[i]:
        hu = i
        break

for i in range(H):
    if '#' in glid[H-i-1]:
        hl = H-i-1
        break

wr, wl = -1, -1

for j in range(W):
    if wl != -1:
        break
    for i in range(H):
        if wl != -1:
            break
        if glid[i][j] == '#':
            wl = j
        
for j in range(W):
    if wr != -1:
        break
    for i in range(H):
        if wr != -1:
            break
        if glid[i][W-j-1] == '#':
            wr = W-j-1

for h in range(hu, hl+1):
    for w in range(wl, wr+1):
        if glid[h][w] == '.':
            print('No')
            exit()

print('Yes')