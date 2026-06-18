N = int(input())
money = 100*(N // 10)
N = N % 10
money += min(15*N, 100)
print(money)