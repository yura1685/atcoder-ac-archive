X = int(input())
n = 0
kane = 100
while True:
    if X <= kane:
        print(n)
        exit()
    else:
        kane = kane*101//100
        n += 1