N, Q = map(int,input().split())
S = list(input())
sta = 0
for i in range(Q):
    t, x = map(int,input().split())
    if t == 1:
        sta = (sta + x) % N
    if t == 2:
        print(S[(x-1-sta) % N])