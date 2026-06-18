import math

M = int(input())
A = []
while M != 0:
    a = min(int(math.log(M,3)),10)
    A.append(a)
    M -= 3**a
print(len(A))
print(*A)