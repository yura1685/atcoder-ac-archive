def f(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
        ans %= (10**9+7)
    return ans

N, M = map(int,input().split())

if abs(N-M) >= 2:
    print(0)
    exit()
hoge = f(N)*f(M)*((N == M) +1)
hoge %= (10**9+7)

print(hoge)