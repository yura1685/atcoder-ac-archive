n=int(input())
M = 0
P = []
for i in range(n):
    y = int(input())
    P.append(y)
    M = max(M,y)

half = 1
price = 0
for i in P:
    if i == M and half == 1:
        price += i//2
        half -= 1
    else:
        price += i
print(price)