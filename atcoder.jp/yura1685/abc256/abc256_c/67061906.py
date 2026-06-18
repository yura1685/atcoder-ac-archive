h1, h2, h3, w1, w2, w3 = map(int,input().split())

ans = 0
for x in range(1,30):
    for y in range(1,30):
        for z in range(1,30):
            for w in range(1,30):
                a, b, c, d = h1-x-y, h2-z-w, w1-x-z, w2-y-w
                if a<1 or b<1 or c<1 or d<1:
                    break
                if h3-c-d == w3-a-b > 0:
                    ans += 1

print(ans)