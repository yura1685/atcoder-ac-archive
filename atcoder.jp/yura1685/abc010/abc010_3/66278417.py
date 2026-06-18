def d(dx, dy):
    return (dx**2+dy**2)**0.5

xa, ya, xb, yb, T, V = map(int,input().split())
n = int(input())
girl = [tuple(map(int,input().split())) for _ in range(n)]

m = 10**10
for x, y in girl:
    dd = d(x-xa,y-ya) + d(x-xb,y-yb)
    m = min(m, dd)

time = m/V
print('YES' if time <= T else 'NO')