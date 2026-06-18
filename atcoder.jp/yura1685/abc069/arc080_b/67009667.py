H, W = map(int,input().split())

def num(n):
    h = n // W
    w = n %  W
    if h % 2 == 1:
        w = W-w-1
    return h, w

N = int(input())
A = list(map(int,input().split()))
color = []
for i in range(N):
    color += [i+1]*A[i]

glid = [[0]*W for _ in range(H)]

for i in range(H*W):
    h, w = num(i)
    glid[h][w] = color[i]

for i in glid:
    print(*i)