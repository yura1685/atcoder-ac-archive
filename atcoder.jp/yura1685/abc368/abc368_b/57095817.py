n = int(input())
c = list(map(int,input().split()))
ans = 0
while True:
    c = sorted(c,reverse = True)
    if c[1] == 0:
        print(ans);exit()
    c[0] -= 1
    c[1] -= 1
    ans += 1