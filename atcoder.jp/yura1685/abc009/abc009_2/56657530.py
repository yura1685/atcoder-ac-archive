N = int(input())
max1 = 0
max2 = 0
for i in range(N):
    A = int(input())
    if max1 < A:
        max2, max1 = max1, A
    elif max2 < A < max1:
        max2 = A
print(max2)