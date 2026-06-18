def f(X):
    a = 1
    while X != 1:
        X //= a
        a += 1
    return a-1

print(f(int(input())))