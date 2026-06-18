from math import isqrt
N = int(input())

def rev(X):
    s = list(str(X))
    s.reverse()
    return int(''.join(s))


if '0' not in str(N) and N == rev(N):
    exit(print(N))

def dfs(n):
    if '0' not in str(n) and n == rev(n):
        return str(n)
    for x in range(2, isqrt(n)+1):
        if n % x == 0 and '0' not in str(x):
            y = rev(x)
            if (n // x) % y == 0:
                z = dfs((n // x) // y)
                if z:
                    return str(x) + '*' + z + '*' + str(y)
    return ''
    
ans = dfs(N)
print(ans if ans else -1)