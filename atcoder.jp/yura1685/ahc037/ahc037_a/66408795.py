N = int(input())
L = [tuple(map(int,input().split())) for _ in range(N)]

print(N)
for a, b in L:
    print(0,0,a,b)