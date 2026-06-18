X = int(input())
N = int(input())

def f(n):
    if n % 3 == 0:
        return n + 1
    elif n % 3 == 1:
        return 2*n
    else:
        return 3*n
    
cnt = 0
while X < N:
    X = f(X)
    cnt += 1

print(cnt)