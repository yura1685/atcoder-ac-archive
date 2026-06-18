N = int(input())
coin = 0
a = 1
while coin < N:
    coin += a
    a += 1
print(a-1)