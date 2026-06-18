import bisect

n, m, x = map(int,input().split())
a = list(map(int,input().split()))
a_x = bisect.bisect(a,x)
print(min(a_x, m-a_x))