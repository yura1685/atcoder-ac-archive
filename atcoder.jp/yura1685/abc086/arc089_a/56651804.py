N = int(input())
now_t, now_x, now_y = 0, 0, 0
for i in range(N):
    t, x, y = map(int,input().split())
    root = abs(now_x - x) + abs(now_y - y)
    if root > t - now_t:
        print('No');exit()
    elif (t - now_t - root) % 2 != 0:
            print('No');exit()
    now_t, now_x, now_y = t, x, y
print('Yes')