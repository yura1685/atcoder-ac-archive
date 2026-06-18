N, M = map(int,input().split())
A = list(map(int,input().split()))
counter = 0
for day in range(1,N+1):
    print(abs(day - A[counter]))
    if day - A[counter] == 0:
        counter += 1