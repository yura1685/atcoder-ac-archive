N = int(input())

def hoge(n):
    num = 0
    for i in range(1,n+1):
        if n % i == 0:
            num += 1
    return num

ans = 0
for n in range(1,N+1,2):
    if hoge(n) == 8:
        ans += 1

print(ans)