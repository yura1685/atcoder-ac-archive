A, B = map(int,input().split())
n = B-A
while n != 0:
    m = B//n - 1
    if A/n <= m:
        print(n)
        exit()
    n -= 1