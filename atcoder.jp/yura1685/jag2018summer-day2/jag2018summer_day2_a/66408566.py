x, y, z = map(int,input().split())

cnt = 0
while True:
    yura = 1000000007*cnt + z
    if yura % 17 == x and yura % 107 == y:
        print(yura)
        exit()
    cnt += 1