N = int(input())
power, i = 1, 1
while i < N+1:
    power = (power*i) % (10**9+7)
    i += 1
print(power)