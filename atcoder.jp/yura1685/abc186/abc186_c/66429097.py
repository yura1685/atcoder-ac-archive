def trans(n):
    hoge = []
    while n != 0:
        m = n % 8
        hoge.append(m)
        n //= 8
    return hoge

N = int(input())

ans = 0
for x in range(1,N+1):
    if '7' not in str(x) and 7 not in trans(x):
        ans += 1

print(ans)