from decimal import Decimal, getcontext
getcontext().prec = 50

p, n = input().split()
p = Decimal('1') - Decimal('2') * Decimal(p)
n = int(n)

ans = Decimal('-0.5') * (p ** n) + Decimal('0.5')
print(ans)