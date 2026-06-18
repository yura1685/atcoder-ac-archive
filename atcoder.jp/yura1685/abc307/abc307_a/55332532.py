N = int(input())
A = list(map(int, input(). split()))
a, b = 0, 0
B = []
for _ in range(N):
    for i in range(7):
        b += A[a+i]
    B.append(b)
    b, a = 0, a + 7
print(*B)