n, k, m = map(int,input().split())
a = list(map(int,input().split()))
score = sum(a)
if n*m - score <= k:
    print(max(0,n*m - score))
else:
    print(-1)