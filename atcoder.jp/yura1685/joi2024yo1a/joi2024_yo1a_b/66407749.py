L = [int(input()) for _ in range(3)]
L.sort()
print(1 if L[2] == L[1] + L[0] else 0)