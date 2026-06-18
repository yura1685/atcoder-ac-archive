n = int(input())
x = [1,1]
for i in range(n):
    x.append(x[-1]+x[-2])
print(x[-2])