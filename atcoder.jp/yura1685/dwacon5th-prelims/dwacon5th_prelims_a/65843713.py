N = int(input())
a = list(map(int,input().split()))
a_bar = sum(a) / N
n = 100
for i in range(N):
    if abs(a_bar-a[i]) < n:
        flame = i
        n = abs(a_bar-a[i])
print(flame)