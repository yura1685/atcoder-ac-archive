N, M = map(int,input().split())
juice = [0] * (M+1)

for _ in range(N):
    _ = int(input())
    X = list(map(int,input().split()))
    for x in X:
        if juice[x] == 0:
            juice[x] = 1
            print(x)
            break
    else:
        print(0)