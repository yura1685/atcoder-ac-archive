N, K = map(int,input().split())

def f(x):
    if x >= K:
        return 0
    else:
        return f(2*x) + 1

ans = 0
for i in range(1,N+1):
    ans += (N*2**f(i))**(-1)

print(ans)