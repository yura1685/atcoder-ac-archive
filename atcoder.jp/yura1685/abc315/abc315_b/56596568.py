m = int(input())
d = list(map(int,input().split()))
middle = (sum(d)+1)//2
month = 1
while sum(d[:month]) < middle:
    month += 1
print(month,middle-sum(d[:month-1]))