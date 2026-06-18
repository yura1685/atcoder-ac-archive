n = int(input())
t = list(map(int,input().split()))
m = int(input())
max_time = sum(t)
for i in range(m):
    p, x = map(int,input().split())
    print(max_time - t[p-1] + x)