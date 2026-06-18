N, K = map(int,input().split())

num = [tuple(map(int,input().split())) for _ in range(N)]
num.sort()

cnt = 0
for a, b in num:
    if cnt + b >= K:
        print(a)
        exit()
    else:
        cnt += b