N = int(input())
money = list(map(int,input().split()))
for i in range(N-1):
    s, t = map(int,input().split())
    x = money[i]//s
    money[i+1] += x*t
print(money[-1])