from math import lcm

N, M = map(int,input().split())
A = list(map(lambda x: int(x)//2,input().split()))

h = 0
a = A[0]
while a % 2 == 0:
    a //= 2
    h += 1
for a in A:
    cnt = 0
    while a % 2 == 0:
        a //= 2
        cnt += 1
    if h != cnt:
        print(0)
        exit()

L = lcm(*A)
print(max(0,(M+L)//(2*L)))