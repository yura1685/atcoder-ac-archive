N = int(input())

x = []

for i in range(1,N+1):
    a, b = map(int,input().split())
    p = 10**20*a//(a+b)
    x.append((p,-i))
        
x.sort(reverse=True)
for i in x:
    print(-i[1], end=' ')