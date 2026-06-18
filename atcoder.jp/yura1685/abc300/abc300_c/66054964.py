H, W = map(int,input().split())

glid = ['.'+input()+'.' for _ in range(H)]
glid = ['.'*(W+2)] + glid + ['.'*(W+2)]

ans = [0]*(min(H,W))

for h in range(1,H+1):
    for w in range(1,W+1):
        if glid[h][w] == '#':
            if glid[h-1][w-1] == glid[h-1][w+1] == glid[h+1][w-1] == glid[h+1][w+1] == '#':
                size = 0
                while glid[h+size][w+size] == '#':
                    size += 1
                size -= 1
                ans[size-1] += 1

print(*ans)