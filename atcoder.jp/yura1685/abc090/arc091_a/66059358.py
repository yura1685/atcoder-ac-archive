N, M = map(int,input().split())
a, b = min(N,M), max(N,M)

if a == 1:
    if b == 1:
        print(1)
    else:
        print(b-2)
elif a == 2:
    print(0)
else:
    print((a-2)*(b-2))