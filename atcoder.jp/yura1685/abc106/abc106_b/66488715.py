N = int(input())

def hoge(n):
    p = 2
    ans = 1
    cnt = 0
    while n != 1:
        if n % p == 0:
            n //= p
            cnt += 1
        else:
            ans *= cnt+1
            cnt = 0
            p += 1
    return ans*(cnt+1)

num = 0
for n in range(1,N+1,2):
    if hoge(n) == 8:
        num += 1

print(num)