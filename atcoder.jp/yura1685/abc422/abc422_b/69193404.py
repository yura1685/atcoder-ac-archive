H, W = map(int,input().split())
S = ['.'*(W+2)] + ['.'+input()+'.' for _ in range(H)] + ['.'*(W+2)]

c = [(-1,0),(0,-1),(0,1),(1,0)]

for h in range(H+2):
    for w in range(W+2):
        if S[h][w] == '.':
            continue
        cnt = 0
        for dh, dw in c:
            if S[h+dh][w+dw] == '#':
                cnt += 1
        if cnt not in (2,4):
            exit(print('No'))

print('Yes')