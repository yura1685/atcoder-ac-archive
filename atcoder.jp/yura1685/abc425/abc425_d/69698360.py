H, W = map(int,input().split())
glid = [['='] + list(input()) + ['='] for _ in range(H)]
glid = [['=']*(W+2)] + glid + [['=']*(W+2)]
s = set()
S = set()
c = [(-1,0),(0,-1),(0,1),(1,0)]

for h in range(H+2):
    for w in range(W+2):
        if glid[h][w] == '#':
            s.add((h,w))

while s:
    for h, w in s:
        for dh, dw in c:
            if glid[h+dh][w+dw] == '.':
                cnt = 0
                for ddh, ddw in c:
                    if glid[h+dh+ddh][w+dw+ddw] == '#':
                        cnt += 1
                if cnt == 1:
                    S.add((h+dh,w+dw))
                else:
                    glid[h+dh][w+dw] = '='
    for h, w in S:
        glid[h][w] = '#'
    s = S.copy()
    S.clear()

ans = 0
for g in glid:
    ans += g.count('#')

print(ans)