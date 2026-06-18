N = int(input())
A = list(map(int,input().split()))
c = [i for i in range(N+1)]
for i in range(1,N+1):
    if c[i] != 0:
        c[A[i-1]] = 0

d = []
for i in c:
    if i != 0:
        d.append(i)
print(len(d))
print(*d)