N = 1000 - int(input())

coin = 0

coin += N//500
N = N % 500

coin += N//100
N = N % 100

coin += N//50
N = N % 50

coin += N//10
N = N % 10

coin += N//5
N = N % 5

coin += N

print(coin)