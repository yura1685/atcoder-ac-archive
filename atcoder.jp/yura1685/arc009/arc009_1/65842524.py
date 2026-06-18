N = int(input())
pay = 0
for _ in range(N):
    a, b = map(int,input().split())
    pay += a*b
print(pay*105//100)