N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

c = 0
a_max = 0
for n in range(N):
    if a[n] > a_max:
        a_max = a[n]
    c = max(c, a_max*b[n])
    print(c)