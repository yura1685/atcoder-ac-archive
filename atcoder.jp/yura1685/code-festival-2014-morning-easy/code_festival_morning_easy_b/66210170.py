n = int(input())
a = (n-1) // 20
b = (n-1)  % 40

if a % 2 == 0:
    print(b+1)
else:
    print(40-b)