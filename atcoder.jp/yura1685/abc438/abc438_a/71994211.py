D, F = map(int,input().split())
x = F
while True:
    x += 7
    if x > D:
        exit(print(x-D))