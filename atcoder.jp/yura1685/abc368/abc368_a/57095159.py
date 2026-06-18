n, k = map(int,input().split())
a = list(map(int,input().split()))
c = a[n-k:]+a[:n-k]
print(*c)