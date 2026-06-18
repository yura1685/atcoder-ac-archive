#a^x mod m を計算する
def axmod(a, x, m):
    result = 1
    a = a % m
    while x > 0:
        if x % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        x //= 2
    return result

a, b = map(int,input().split())
print(axmod(a,b,1000000007))