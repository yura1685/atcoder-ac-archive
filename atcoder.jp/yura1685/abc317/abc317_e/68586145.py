H, W = map(int,input().split())

A = [['#']*(W+2)] + [['#']+list(input())+['#'] for _ in range(H)] + [['#']*(W+2)]

for i in range((H+2)*(W+2)):
    h, w = divmod(i,W+2)
    if A[h][w] == 'S':
        sh, sw = h, w
    if A[h][w] not in '<>^v':
        continue
    if A[h][w] == '^':
        for i in range(h-1,-1,-1):
            if A[i][w] in '.!':
                A[i][w] = '!'
            else:
                break
    elif A[h][w] == 'v':
        for i in range(h+1,H+2):
            if A[i][w] in '.!':
                A[i][w] = '!'
            else:
                break
    elif A[h][w] == '<':
        for i in range(w-1,-1,-1):
            if A[h][i] in '.!':
                A[h][i] = '!'
            else:
                break
    elif A[h][w] == '>':
        for i in range(w+1,W+2):
            if A[h][i] in '.!':
                A[h][i] = '!'
            else:
                break

from collections import deque

c = [(-1,0),(0,-1),(0,1),(1,0)]
A[sh][sw] = 0
d = deque([(sh,sw)])
while d:
    h, w = d.popleft()
    for dh, dw in c:
        if A[h+dh][w+dw] == 'G':
            exit(print(A[h][w]+1))
        elif A[h+dh][w+dw] == '.':
            A[h+dh][w+dw] = A[h][w] + 1
            d.append((h+dh,w+dw))

print(-1)