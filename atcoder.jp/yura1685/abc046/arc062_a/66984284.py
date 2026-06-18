N = int(input())
T, A = map(int,input().split())

for _ in range(N-1):
    t, a = map(int,input().split())
    c = max((T+t-1)//t, (A+a-1)//a)
    T, A = c*t, c*a

print(T+A)