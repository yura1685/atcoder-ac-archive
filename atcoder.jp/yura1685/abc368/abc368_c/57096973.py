N = int(input())
H = list(map(int,input().split()))
now_enemy = 0
t = 0
while True:
    if H[-1] <= 0:
        print(t);exit()
    u = H[now_enemy] // 5
    t += 3*u
    H[now_enemy] -= 5*u
    while H[now_enemy] > 0:
        if (t+1) % 3 == 0:
            H[now_enemy] -= 3
            t += 1
        else:
            H[now_enemy] -= 1
            t += 1
    now_enemy += 1