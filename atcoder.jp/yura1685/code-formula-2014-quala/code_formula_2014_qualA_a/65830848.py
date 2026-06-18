N = int(input())
root = round(N ** (1/3))
if root ** 3 == N:
    print("YES")
else:
    print("NO")