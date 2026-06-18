mod = 10**9 + 7
def fib(n):
    a, b = 1, 1
    for _ in range(n-2):
        a, b = b, (a+b) % mod
    print(b)

fib(int(input()))