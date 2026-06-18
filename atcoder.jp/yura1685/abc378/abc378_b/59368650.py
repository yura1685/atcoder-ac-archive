N = int(input())
gomi = []
for i in range(N):
    q, r = map(int,input().split())
    gomi.append([q,r])
Q = int(input())
for i in range(Q):
    t, d = map(int,input().split())
    q, r = gomi[t-1][0], gomi[t-1][1]
    a = d % q
    if a == r:
        print(d)
    elif a > r:
        print(d+r-a+q)
    else:
        print(d+r-a)