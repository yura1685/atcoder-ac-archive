m, n, N = map(int,input().split())
make = N
while N >= m:
    k = N // m * n
    make += k
    N = N % m + k
print(make)