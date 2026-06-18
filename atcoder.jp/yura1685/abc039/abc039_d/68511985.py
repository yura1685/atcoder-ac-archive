H, W = map(int,input().split())
S = [list(input()) for _ in range(H)]

make = [['.']*W for _ in range(H)]

c = [(-1,-1),(-1,0),(-1,1),
     ( 0,-1),( 0,0),( 0,1),
     ( 1,-1),( 1,0),( 1,1)]

for h in range(H):
    for w in range(W):
        flag = True
        for dh, dw in c:
            if 0 <= h + dh < H and 0 <= w + dw < W:
                if S[h+dh][w+dw] == '.':
                    flag = False
                    break
        if flag:
            make[h][w] = '#'

ans = [['.']*W for _ in range(H)]

for h in range(H):
    for w in range(W):
        if make[h][w] == '.':
            continue
        for dh, dw in c:
            if 0 <= h + dh < H and 0 <= w + dw < W:
                ans[h+dh][w+dw] = '#'

if ans == S:
    print('possible')
    for i in make:
        print(''.join(i))

else:
    print('impossible')