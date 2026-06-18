def f(n):
    if n == 0:
        return 1
    else:
        return n*f(n-1)

P = int(input())
coin = [f(10),f(9),f(8),f(7),f(6),f(5),f(4),f(3),f(2),f(1)]
pay = 0

for i in range(10):
    a = P//coin[i]
    P -= a*coin[i]
    pay += a
print(pay)