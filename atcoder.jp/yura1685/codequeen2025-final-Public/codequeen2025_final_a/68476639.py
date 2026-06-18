N = int(input())
lst = sorted(tuple(map(int,input().split())) for _ in range(N))
for m, d in lst:
    print(m,d)