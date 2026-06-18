from bisect import bisect_left

N, M = map(int,input().split())
X, Y = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

time  = 0      # 現在時刻
place = 0      # 0だったらa空港,1だったらb空港にいる
ride  = 0      # 搭乗回数
while True:
    if not place:
        if time > a[-1]:
            break
        time = a[bisect_left(a,time)] + X
        place = 1
        ride += 1
    else:
        if time > b[-1]:
            break
        time = b[bisect_left(b,time)] + Y
        place = 0
        ride += 1
print(ride//2)