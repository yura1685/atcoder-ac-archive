N = int(input())

black = []
for i in range(N):
    a,b,c,d = map(int,input().split())
    for x in range(a,b):
        for y in range(c,d):
            black.append((x,y))
print(len(set(black)))