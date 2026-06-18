N = int(input())
a = list(map(int,input().split()))

love = 0

for i in range(N):
    x = a[i]
    if a[x-1] == i+1:
        love += 1
print(love//2)