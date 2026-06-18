N = int(input())
d = sorted(list(map(int,input().split())))
a, b = d[N//2-1], d[N//2]
print(b-a)