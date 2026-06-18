n = int(input())
c = [[*map(int, input().split())] for _ in range(n)]

m = min(c[i][0] for i in range(n))
a = [c[i][0] - m for i in range(n)]
b = [c[0][j] - a[0] for j in range(n)]

def check():
    for i in range(n):
        for j in range(n):
            if c[i][j] != a[i] + b[j]:
                return False
    return True

if check():
    print('Yes')
    print(*a)
    print(*b)
else:
    print('No')
