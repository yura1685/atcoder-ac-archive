H, W = map(int,input().split())
glid = ['']*(H+2)
for i in range(1,H+1):
    glid[i] = list('.'+input()+'.')
glid[0], glid[H+1] = ['.']*(W+2), ['.']*(W+2)

for h in range(1,H+1):
    for w in range(1,W+1):
        c = ['1','2','3','4','5']
        x = []
        if glid[h][w] == '.':
            x.append(glid[h-1][w])
            x.append(glid[h][w-1])
            x.append(glid[h][w+1])
            x.append(glid[h+1][w])
            for i in c:
                if i not in x:
                    glid[h][w] = i
                    break
glid = glid[1:-1]
for i in glid:
    j = i[1:-1]
    print(''.join(j))