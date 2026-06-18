N, D = map(int,input().split())
X, Y = map(int,input().split())
if X % D or Y % D: exit(print(0))
X, Y = X//D, Y//D
if X < 0: X = -X
if Y < 0: Y = -Y
if (X+Y+N) % 2 or N < X+Y : exit(print(0))

from math import factorial as fact

ans = 0
for A in range(X,N-Y+1,2):
    B = N - A
    s, t, u, v = (A+X)//2, (A-X)//2, (B+Y)//2, (B-Y)//2
    ans += fact(N)//(fact(s)*fact(t)*fact(u)*fact(v))

print(ans/pow(4,N))