N = int(input())
n = len(str(N))
if n % 2 == 1:
    N = 10**(n-1)-1
    n -= 1

u = N//(10**(n//2))
v = N % (10**(n//2))
print(u - (u > v))