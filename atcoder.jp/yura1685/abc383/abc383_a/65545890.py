N = int(input())
now = 0
last = 0
for i in range(N):
    T, V = map(int,input().split())
    now = max(now-(T-last),0) + V
    last = T
print(now)