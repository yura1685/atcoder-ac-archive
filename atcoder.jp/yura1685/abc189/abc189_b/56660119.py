N, X = map(int,input().split())
alcohol = X*100
num = 0
for i in range(N):
    V, P = map(int,input().split())
    alcohol -= V*P
    num += 1
    if alcohol < 0:
        print(num)
        exit()
print(-1)