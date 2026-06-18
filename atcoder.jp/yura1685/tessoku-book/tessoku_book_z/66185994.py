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

# ミラーラビン
def miller_rabin_base(n, a):
    if n % a == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    x = axmod(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(s - 1):
        x = axmod(x, 2, n)
        if x == n - 1:
            return True
    return False

# 素数判定
def is_prime(n):
    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    for base in [2, 7, 61]:
        if base >= n:
            continue
        if not miller_rabin_base(n, base):
            return False
    return True

Q = int(input())
for _ in range(Q):
    x = int(input())
    if is_prime(x):
        print('Yes')
    else:
        print('No')