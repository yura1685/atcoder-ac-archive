M, D = map(int, input().split())
y, m, d = map(int, input().split())
if d == D:
    m, d = m + 1, 1
    if m == M +1 :
        y, m = y + 1, 1
    print(y, m, d, sep=' ')
    exit()
else:
    print(y, m, d+1, sep=' ')