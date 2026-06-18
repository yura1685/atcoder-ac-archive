N = int(input())
num = 0
for _ in range(N):
    T, A = map(str,input().split())
    a = int(A)
    if T == '+':
        num += a
        num %= 10000
    elif T == '-':
        num -= a
        num %= 10000
    else:
        num *= a
        num %= 10000
    print(num)