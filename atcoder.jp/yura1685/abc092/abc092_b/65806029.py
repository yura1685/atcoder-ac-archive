N = int(input())
D, X = map(int,input().split())
eat = 0
for i in range(N):
    A = int(input())
    eat += int((D-1)/A) + 1
print(X+eat)