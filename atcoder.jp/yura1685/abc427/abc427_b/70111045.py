N = int(input())

def f(n):
    res = 0
    for i in str(n):
        res += int(i)
    return res

A = [1]
for _ in range(N):
    s = 0
    for a in A:
        s += f(a)
    A.append(s)

print(A[-1])