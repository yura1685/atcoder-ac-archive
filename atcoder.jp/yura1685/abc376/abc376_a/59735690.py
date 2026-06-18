N, C = map(int,input().split())
T = list(map(int,input().split()))
last_time = T[0]
candy = 1
for i in range(N-1):
    if T[i+1]-last_time >= C:
        candy += 1
        last_time = T[i+1]
print(candy)