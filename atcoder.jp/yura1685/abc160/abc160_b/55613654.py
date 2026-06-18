X = int(input())
coin500 = X // 500
X = X % 500
coin5 = X // 5
print(coin500 * 1000 + coin5 * 5)