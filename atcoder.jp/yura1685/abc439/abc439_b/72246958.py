def happy(n:int) -> int:
    X = str(n)
    res = 0
    for x in X:
        res += int(x) ** 2
    return res

N = int(input())

for _ in range(100000):
    N = happy(N)

print('Yes' if N == 1 else 'No')