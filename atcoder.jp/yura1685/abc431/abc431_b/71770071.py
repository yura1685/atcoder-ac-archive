X = int(input())
N = int(input())
W = list(map(int,input().split()))
Q = int(input())
cnt = [0] * N
for _ in range(Q):
    P = int(input()) - 1
    if cnt[P] == 0:
        X += W[P]
        cnt[P] = 1
    else:
        X -= W[P]
        cnt[P] = 0
    print(X)