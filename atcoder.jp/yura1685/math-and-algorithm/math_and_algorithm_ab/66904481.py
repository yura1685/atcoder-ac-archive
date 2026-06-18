def fib(n):
    c = [1,1]
    for _ in range(n-1):
        c.append(c[-1]+c[-2])
    return c[n]

print(fib(int(input())))