N, M = map(int,input().split())
a = [int(input()) for _ in range(M)]
a = [-1] + a + [N+1]
b = [a[i+1]-a[i]-1 for i in range(M+1)]

F = max(b)
fib = [0,1,1,2]
for i in range(F-3):
    n = (fib[-1]+fib[-2]) % (10**9+7)
    fib.append(fib[-1]+fib[-2])

ans = 1
for x in b:
    ans *= fib[x]
    ans %= 10**9+7

print(ans)