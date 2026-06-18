def prime(n):
    p = 2
    while n != 1:
        if n % p == 0:
            if n // p == 1:
                return 'prime'
            else:
                return 'gomi'
        p += 1

X = int(input())
for p in range(X,100004):
    if prime(p) == 'prime':
        print(p)
        exit()