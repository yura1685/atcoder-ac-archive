D, N = map(int,input().split())

day = [24]*D
for _ in range(N):
    L, R, H = map(int,input().split())
    for i in range(L-1,R):
        day[i] = min(day[i],H)
print(sum(day))