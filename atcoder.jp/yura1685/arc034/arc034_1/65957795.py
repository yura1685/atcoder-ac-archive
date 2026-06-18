N = int(input())
m = 0
for _ in range(N):
    a,b,c,d,e = map(int,input().split())
    score = a+b+c+d+110/900*e
    m = max(m,score)
print(m)