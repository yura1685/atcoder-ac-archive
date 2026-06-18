N = int(input())
c = N // 9
base = (10**(c+1)-1)//9
n = N % 9
if n == 0:
    n = 9
    base = (10**c-1)//9
print(base*n)