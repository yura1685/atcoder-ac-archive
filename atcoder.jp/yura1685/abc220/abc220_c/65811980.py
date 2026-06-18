N = int(input())
A = list(map(int,input().split()))
X = int(input())
s = sum(A)

count = N*(X//s)
X -= (X//s)*s

now = 0
while X >= 0:
    X -= A[now]
    now += 1
    count += 1
print(count)