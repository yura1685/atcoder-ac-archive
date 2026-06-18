from collections import deque
from copy import deepcopy

H, W = map(int,input().split())
maze = ([['#']*(W+2)] + 
        [['#'] + list(input()) + ['#'] for _ in range(H)] +             
        [['#']*(W+2)])

flag = False
for h in range(H+2):
    for w in range(W+2):
        if maze[h][w] == 'S':
            sh, sw = h, w
            flag = True
            break
    if flag:
        break

maze[sh][sw] = '0'
ans = H*W

for d in [deque([(sh,sw,'-')]), deque([(sh,sw,'|')])]:
    glid = deepcopy(maze)
    while d:
        h, w, m = d.popleft()
        if m == '-':
            if glid[h+1][w] in '.G':
                if glid[h+1][w] == 'G':
                    ans = min(ans,int(glid[h][w])+1)
                    break
                d.append((h+1,w,'|'))
                glid[h+1][w] = str(int(glid[h][w]) + 1)
            if glid[h-1][w] in '.G':
                if glid[h-1][w] == 'G':
                    ans = min(ans,int(glid[h][w])+1)
                    break
                d.append((h-1,w,'|'))
                glid[h-1][w] = str(int(glid[h][w]) + 1)
        else:
            if glid[h][w+1] in '.G':
                if glid[h][w+1] == 'G':
                    ans = min(ans,int(glid[h][w])+1)
                    break
                d.append((h,w+1,'-'))
                glid[h][w+1] = str(int(glid[h][w]) + 1)
            if glid[h][w-1] in '.G':
                if glid[h][w-1] == 'G':
                    ans = min(ans,int(glid[h][w])+1)
                    break
                d.append((h,w-1,'-'))
                glid[h][w-1] = str(int(glid[h][w]) + 1)

print(ans if ans < H*W else -1)