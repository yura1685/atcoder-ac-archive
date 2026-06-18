N = int(input())
A = list(map(int,input().split()))
ans = max(A)
while max(A) == ans:
    A.remove(max(A))
print(max(A))