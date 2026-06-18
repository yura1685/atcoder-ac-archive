T = int(input())
for _ in range(T):
    L, R = map(int,input().split())
    if 2*L > R:
        print(0)
    else:
        c = R - 2*L
        print((c+1)*(c+2)//2)