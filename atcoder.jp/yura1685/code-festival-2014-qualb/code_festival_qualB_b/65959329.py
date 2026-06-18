N, K = map(int,input().split())
walk = 0
for day in range(1,N+1):
    a = int(input())
    walk += a
    if walk >= K:
        print(day)
        walk -= 10**18