N = int(input())
b = 0
ans = N
while 2**b <= N:
    a = N // (2**b)
    c = N - a*2**b
    ans = min(ans,a+b+c)
    b += 1
print(ans)