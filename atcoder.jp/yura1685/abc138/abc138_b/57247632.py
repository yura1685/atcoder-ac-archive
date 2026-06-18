n = int(input())
a = list(map(int,input().split()))
c = 0
for i in a:
    c += 1/i
print(1/c)