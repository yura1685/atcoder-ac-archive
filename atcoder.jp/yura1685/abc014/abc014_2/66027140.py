def nisinsuu(n):
    return list(reversed([int(digit) for digit in bin(n)[2:]]))

n, X = map(int,input().split())
a = list(map(int,input().split()))

x = nisinsuu(X)

pay = 0
for i in range(len(x)):
    if x[i] == 1:
        pay += a[i]

print(pay)