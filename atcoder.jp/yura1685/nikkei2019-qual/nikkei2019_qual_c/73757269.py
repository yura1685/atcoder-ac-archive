N = int(input())
P = []
B = 0
for _ in range(N):
    a, b = map(int,input().split())
    P.append(a+b)
    B += b 
P.sort(reverse=True)
print(sum(P[::2]) - B)