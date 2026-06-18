N = int(input())
m = 10**9+1
h = 0
for _ in range(N):
    a, b = map(int,input().split())
    if b < m:
        m = b
        h = a

print(m+h)