N = int(input()) - 2
a, b = 1, 1
mod = 10**9 + 7
while N:
    c = (a+b) % mod
    a, b = b, c
    N -= 1
print(b)