def clock_1minlater(h,m):
    m += 1
    if m == 60:
        h += 1
        m = 0
    if h == 24:
        h = 0
    return h, m

def kasu(h,m):
    if 0 <= h <= 9:
        h = '0' + str(h)
    if 0 <= m <= 9:
        m = '0' + str(m)
    h, m = str(h), str(m)
    h, m = h[0] + m[0], h[1] + m[1]
    if 0 <= int(h) <= 23 and 0 <= int(m) <= 59:
        return True
    return False

H, M = map(int,input().split())
for i in range(10000000000000000000000000000000):
    if kasu(H,M):
        print(H,M)
        exit()
    H, M = clock_1minlater(H,M)