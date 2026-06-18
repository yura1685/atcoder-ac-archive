N, K = map(int,input().split())
h = list(map(int,input().split()))
ride = 0
for i in range(N):
    if h[i] >= K:
        ride += 1
print(ride)