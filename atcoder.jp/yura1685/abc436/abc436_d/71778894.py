H, W = map(int,input().split())
glid = [['#'] + list(input()) + ['#'] for _ in range(H)]
glid = [['#']*(W+2)] + glid + [['#']*(W+2)]

def O(x:str): return ord(x)-97

alp = [[] for _ in range(26)]

for h in range(H+2):
    for w in range(W+2):
        if glid[h][w] not in ".#":
            alp[O(glid[h][w])].append((h,w))

from collections import deque
inf = float('inf')
T = [[inf]*(W+2) for _ in range(H+2)]
T[1][1] = 0
d = deque([(1,1)])
c = [(-1,0),(0,-1),(0,1),(1,0)]
while d:
    h, w = d.popleft()
    for dh, dw in c:
        if glid[h+dh][w+dw] != '#' and T[h][w] + 1 < T[h+dh][w+dw]:
            d.append((h+dh,w+dw))
            T[h+dh][w+dw] = T[h][w] + 1
    if glid[h][w] not in '.#':
        for h2, w2 in alp[O(glid[h][w])]:
            if T[h][w] + 1 < T[h2][w2]:
                d.append((h2,w2))
                T[h2][w2] = T[h][w] + 1
            glid[h2][w2] = '.'

print(T[H][W] if T[H][W] < inf else -1)