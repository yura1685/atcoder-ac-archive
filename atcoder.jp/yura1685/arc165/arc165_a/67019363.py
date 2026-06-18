def f(n):
    prime = []
    for p in range(2,int(n**(1/2))+2):
        if n % p == 0:
            while n != 1:
                if n % p == 0:
                    n //= p
                else:
                    return True
            return False
    return False

T = int(input())
for _ in range(T):
    N = int(input())
    c = f(N)
    if not c:
        print('No')
    else:
        print('Yes')