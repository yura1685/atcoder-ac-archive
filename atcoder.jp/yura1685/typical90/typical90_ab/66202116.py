N = int(input())

glid = [[0]*1002 for _ in range(1002)]

for _ in range(N):
    lx, ly, rx, ry = map(int,input().split())
    glid[ly][lx] += 1
    glid[ly][rx] -= 1
    glid[ry][lx] -= 1
    glid[ry][rx] += 1

for h in range(1001):
    for w in range(1001):
        glid[h][w+1] += glid[h][w]

for w in range(1001):
    for h in range(1001):
        glid[h+1][w] += glid[h][w]

paper = [0]*(N+1)
for h in range(1001):
    for w in range(1001):
        paper[glid[h][w]] += 1

for i in range(1,N+1):
    print(paper[i])