N = int(input())

A = list(map(int,input().split()))

s, s2 = 0, 0
for a in A:
    s += a
    s2 += a*a

print(N*s2 - s*s)