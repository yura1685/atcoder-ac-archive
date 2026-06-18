N = int(input())
po = [tuple(map(int,input().split())) for _ in range(N)]

ans = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            x1, y1 = po[i]
            x2, y2 = po[j]
            x3, y3 = po[k]
            x2, y2, x3, y3 = x2-x1, y2-y1, x3-x1, y3-y1
            X = abs(x2*y3 - x3*y2)
            if X and X % 2 == 0:
                ans += 1
print(ans)