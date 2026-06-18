N = int(input())
push = 0

A, B = [], []
for _ in range(N):
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)

for i in range(N):
    a, b = A[-i-1], B[-i-1]
    a += push
    push += (b - (a % b)) % b

print(push)