A, K = map(int,input().split())

if K == 0:
    print(2000000000000 - A)
    exit()

day = 0
while A < 2000000000000:
    A += 1+K*A
    day += 1

print(day)