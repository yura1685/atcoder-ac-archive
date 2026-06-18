N = int(input())

while N != 1:
    if N % 2 != 0 and N %3 != 0:
        print('No')
        exit()
    if N % 2 == 0:
        N = N // 2
    if N % 3 == 0:
        N = N // 3
print('Yes')