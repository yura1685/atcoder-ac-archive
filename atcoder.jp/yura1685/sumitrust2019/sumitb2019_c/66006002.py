X = int(input())
n2 = X % 100
m = X // 100

if n2 == 0:
    print(1)
    exit()

x = (n2-1) // 5
if m-1 >= x:
    print(1)

else:
    print(0)