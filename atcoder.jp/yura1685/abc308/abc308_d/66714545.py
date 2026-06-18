from collections import deque

H, W = map(int,input().split())
S = [list('#'+input()+'#') for _ in range(H)]
S = [['#']*(W+2)] + S + [['#']*(W+2)]

c = [(-1,0),(0,-1),(1,0),(0,1)]
dic = {'s':'n','n':'u','u':'k','k':'e','e':'s'}

if S[1][1] != 's':
    print('No')
    exit()

check = [[0]*(W+2) for _ in range(H+2)]
check[1][1] = 1

d = deque([(1,1)])
while d:
    h, w = d.popleft()
    for dh, dw in c:
        if S[h+dh][w+dw] == dic[S[h][w]] and check[h+dh][w+dw] == 0:
            check[h+dh][w+dw] = 1
            if (h+dh,w+dw) == (H,W):
                print('Yes')
                exit()
            d.append((h+dh,w+dw))

print('No')